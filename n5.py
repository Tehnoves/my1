from ctypes import *
libc = CDLL('msvcrt.dll')
libc.printf(b"Hello world\n")
message_string = 'Hello world\n'
libc.printf(b"Testing: hello world")