# sys_operations.py
import platform
import socket
import os

print("Machine type: ")
print(platform.machine())

print("Processor type: ")
print(platform.architecture())

socket.setdefaulttimeout(50)
print("Get the default Socket Timeout in seconds")
print(socket.getdefaulttimeout())

print("OS Type: ")
print(os.name)

print("OS Name: ")
print(os.system())