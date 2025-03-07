# sys_operations.py
import platform
import socket
import os

print("Machine type: ")
print(platform.machine(), "\n")

print("Processor type: ")
print(platform.architecture(), "\n")

socket.setdefaulttimeout(50)
print("Get the default Socket Timeout in seconds")
print(socket.getdefaulttimeout(), "\n")

print("OS Type: ")
print(os.name, "\n")

print("OS Name: ")
print(platform.system(), "\n")

print("Current PID: ")
print(os.getpid(), "\n")