from pwn import *

conn = remote('13.212.234.124', '9999')

z = int(conn.recvuntil(b'\n').strip()[4:].decode())
N = int(conn.recvuntil(b'\n').strip()[4:].decode())

totient = z // (z // N + 1)
conn.sendline(str(totient).encode())
conn.interactive()