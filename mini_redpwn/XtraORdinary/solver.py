out = "57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637"
out_s = "".join(chr(int(out[i*2:i*2+2], 16)) for i in range(len(out)//2))

random_strs = [
    'my encryption method',
    'is absolutely impenetrable',
    'and you will never',
    'ever',
    'break it'
]

def encrypt(ptxt, key):
    ctxt = ""
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += chr(ord(a) ^ ord(b))
    return ctxt

#for i in range(2**len(random_strs)):
i = 28
res = out_s
for j in range(len(random_strs)):
    if i >> j & 1 == 1:
        res = encrypt(res, random_strs[j])
#print(encrypt(res, "picoCTF{"))
print(i)
print(encrypt(res, "Africa!"))



