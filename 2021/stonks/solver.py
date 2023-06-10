if __name__ == "__main__":
    inp = open("input.txt").read().strip()
    print(inp)
    print("".join(inp[i*4:(i+1)*4][::-1] for i in range(len(inp)//4)))
