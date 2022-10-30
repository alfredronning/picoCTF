inp = open("message.txt").read()
res = ""
for i in range(len(inp)//3):
    res += inp[i*3+2]
    res += inp[i*3:i*3+2]
print(res)
