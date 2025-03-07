# sys_operations.py
import platform
import socket
import os
import sys

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

file_name = "fdpractice.txt"
file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)
print(f"\n[Process {os.getgid()}] Opened file_handle: {file_handle}")

file_object_TextIO = os.fdopen(file_handle, "w+")
file_object_TextIO.write("Some string to write to the file")
file_object_TextIO.flush()

pid = os.fork()

if pid == 0:
    print(f"\n[Child process {os.getpid()}], [Parent Process {os.getppid()}]")
    os.lseek(file_handle, 0, 0)

    print(f"[ File Content: {os.read(file_handle, 100).decode()} ]")
    os.close(file_handle)
    sys.exit(0)