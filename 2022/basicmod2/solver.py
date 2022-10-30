message = open("message.txt").read()

modinvs = [pow(int(c), -1, 41) for c in message.split()]
print(modinvs)

def translate(c):
    if c <= 26:
        return chr(c+ord("a")-1)
    elif c <= 36:
        return chr(c-25+ord("0")-2)
    else:
        return "_"

print("picoCTF{" + "".join(translate(m) for m in modinvs) + "}")

