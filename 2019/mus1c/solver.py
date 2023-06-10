if __name__ == "__main__":
    inp = open("input.txt").read().strip().split("\n")
    print("".join(chr(int(i)) for i in inp))

