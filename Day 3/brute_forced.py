def lcomb(bank):
    largest = int(bank[0:2])
    l = len(bank)
    for i, f in enumerate(bank[0:l-1]):
        for s in bank[i+1:]:
            if largest < int(f + s):
                largest = int(f + s)
    return largest

def main():
    t_joltage = 0
    with open("input.txt", "r") as file:
        for line in file:
            t_joltage += lcomb(line.strip())
    print(t_joltage)
    return 0

if __name__ == "__main__":
    main()
