# sys_operations.py
import platform
import socket

print("Machine type: ")
print(platform.machine())

print("Processor type: ")
print(platform.architecture())

socket.setdefaulttimeout(50)
print("Get the default Socket Timeout in seconds")
print(socket.getdefaulttimeout())