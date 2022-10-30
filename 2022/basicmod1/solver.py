text = open("message.txt").read()
mods = [int(c)%37 for c in text.split()]

def translate(c):
    if c <= 25:
        return chr(c+ord("A"))
    elif c <= 35:
        return chr(c+ord("0")-26)
    else:
        return "_"

print("picoCTF{" + "".join(translate(m) for m in mods)+ "}")
