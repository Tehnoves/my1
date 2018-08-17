from ctypes import *
libc = CDLL('msvcrt.dll')
libc.printf(b"Hello world\n")
message_string = 'Hello world\n'
libc.printf(b"Testing: hello world")
print(c_ushort(-3)) 
#  git log --pretty=oneline