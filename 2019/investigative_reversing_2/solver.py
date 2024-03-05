def decode_bits(bits):
    bitstring = "".join(str(b) for b in bits[::-1])
    return chr(int(bitstring, 2)+5)

if __name__ == "__main__":
    img = open("encoded.bmp", "rb").read()
    bits_rev = [b&1 for b in img[2000:2400]]
    flag = "".join(decode_bits(bits_rev[i*8:(i+1)*8]) for i in range(50))
    print(flag)

