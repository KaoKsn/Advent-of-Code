import sys
def ifFresh(id, freshRange):
    id = int(id)
    for r in freshRange:
        start, end = map(int, r.split('-'))
        if id in range(start, end + 1):
            return True
    return False

def main():
    freshCount = 0
    freshRange = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            if line == '\n':
                break
            freshRange.append(line.strip())
        for line in file:
            if ifFresh(line.strip(), freshRange):
                freshCount += 1
    print("Total fresh items:", freshCount)
    return 0

if __name__ == "__main__":
    main()
