if __name__ == "__main__":
    nums = open("input.txt").read().strip().split("\n")
    res = [chr(int(i)) for i in nums]
    print("".join(res))
