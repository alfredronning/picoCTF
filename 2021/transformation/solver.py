if __name__ == "__main__":
    inp = open("enc").read().strip()
    res = ""
    for i in inp:
        chrval = ord(i)
        first_chr = chrval >> 8
        second_chr = chrval & 0xff
        res += chr(first_chr) + chr(second_chr)
    print(res)

