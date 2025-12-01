def decoder(val, prev):
    op = val[0]
    rot = int(val[1:])
    if (op == 'L'):
        return (prev - rot) % 100
    else:
        return (prev + rot) % 100

def main():
    n = 0
    prev = 50
    with open("input.txt", "r") as file:
        for line in file:
            prev = decoder(line.strip(), prev)
            if (prev == 0):
                n += 1
    print("Password:" , n)
    return 0

if __name__ == "__main__":
    main()

