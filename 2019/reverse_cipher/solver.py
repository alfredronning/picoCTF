if __name__ == "__main__":
    rev = open("rev_this").read().strip()
    flag = rev[:8]
    for i in range(8, 0x17):
        current_c = ord(rev[i])
        if i & 1 == 0:
            current_c -= 5
        else:
            current_c += 2
        flag += chr(current_c)
    flag += "}"
    print(flag)
