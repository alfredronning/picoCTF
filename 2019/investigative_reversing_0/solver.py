if __name__ == "__main__":
    inp = open("input.txt").read().strip()
    res = inp[:6]
    for i in range(6, 0xf):
        res += chr(ord(inp[i])-5)
    print(res)
    res += chr(ord(inp[0xf])+3)
    for i in range(0x10, 0x1a):
        res += chr(ord(inp[i]))
        print(res)
    print(res)
