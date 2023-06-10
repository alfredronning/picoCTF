from pwn import *

a_enc = bytes.fromhex("23666b6f3a3c1a111d3971771d397122181d3927731d3925231d3924241d3924")
flag_enc = bytes.fromhex("51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57")
a_s = b"A"*32

key = xor(a_enc, a_s)

print(key)
print(xor(key, flag_enc).decode())
