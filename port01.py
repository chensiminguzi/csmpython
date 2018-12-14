import socket

portScan=socket.socket()
# portScan.sittimeout(3)
# host=input("Please input host:")
port=input("Please input port:")
try:
    portScan.connect(("192.168.252.13",int(port)))
    print(portScan.recv(1024).decode("utf-8"))
    portScan.close()
except Exception as e:
    print("error scan:",e)
