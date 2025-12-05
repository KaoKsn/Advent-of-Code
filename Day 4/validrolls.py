import sys

def validRollsIn(grid):
    validrolls, rows = 0, len(grid)
    col = len(grid[0])
    # Traverse through the matrix.
    for r in range(0, rows):
        for c in range(0, col):
            # If a paper roll exists, check its neighbours.
            if grid[r][c] == '@':
                neighbourrolls = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        # Don't count the roll itself.
                        if i == 0 and j == 0:
                            continue
                        # Ensure index in bounds.
                        elif 0 <= r + i < rows and 0 <= c + j < col:
                            if grid[r + i][c + j] == '@':
                                neighbourrolls += 1
                if neighbourrolls < 4:
                    validrolls += 1
    return validrolls

def main():
    if (len(sys.argv) != 2):
        print("Usage: python validrolls.py inputfile")
        return 1
    validRolls = 0
    grid = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            grid.append(line.strip())
        validRolls = validRollsIn(grid)
    print("Total valid rolls:", validRolls)
    return 0

if __name__ == "__main__":
    main()
