import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc

def b16_decode(enc):
    dec = ""
    for i in range(len(enc)//2):
        first = enc[i*2]
        second = enc[i*2+1]
        first_idx = ALPHABET.index(first)
        second_idx = ALPHABET.index(second)
        dec += chr((first_idx << 4) + second_idx)
    return dec

def encode(flag, key):
    b16 = b16_encode(flag)
    enc = ""
    for i, c in enumerate(b16):
        enc += shift(c, key[i % len(key)])
    return enc

def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]

def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]


def decode(s, key):
    dec = ""
    for i, c in enumerate(s):
        dec += unshift(c, key[i % len(key)])
    return b16_decode(dec)


b16 = "lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"
for k in ALPHABET:
    dec = decode(b16, k)
    print(dec)
