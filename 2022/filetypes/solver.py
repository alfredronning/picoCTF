flag = open("flag").read()
print("".join(chr(int(flag[i*2:i*2+2], 16)) for i in range(len(flag)//2)))
