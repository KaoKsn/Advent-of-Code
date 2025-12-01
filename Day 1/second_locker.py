# Count the number of times the dial finds 0 (even during rotations)
def decoder(val, prev):
    op = val[0]
    rot = int(val[1:])
    if (op == 'L'):
        # when prev is 0, 100 - 0 is 100 which adds an extra value to number of 0s encountered.
        if prev == 0:
            prev = 100
            # (-rot) % 100 = (100 - rot) % 100. so this is not going to affect return pos.
        return [(prev - rot) % 100, (rot + (100 - prev)) // 100]
    else:
        # rot + prev // 100 -> total times 0 is encountered (including currently pointing to 0)
        return [(prev + rot) % 100, (rot + prev) // 100]
    # return [pos, times_0_encountered]

def main():
    n = 0
    prev = 50
    with open("input.txt", "r") as file:
        for line in file:
            prev, inc = decoder(line.strip(), prev)
            n += inc
    print("Password:" , n)
    return 0

if __name__ == "__main__":
    main()

