import socket

target_host  = "www.gerobakoe.com"
target_port = 80


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send("GET / HTTP/1.1\r\nHost: gerobakoe.com\r\n\r\n")
response = client.recv(4096)

print (response)