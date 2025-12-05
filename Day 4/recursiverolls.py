import sys

def allValidRollsIn(grid):
    allrolls = 0
    # Check for valid rolls in a grid until there are none.
    while True:
        prevrolls = allrolls
        allrolls += validRolls(grid)
        # If no rolls were picked, quit.
        if allrolls == prevrolls:
            break
    return allrolls

def validRolls(grid):
    validrollindex = []
    validrolls, rows = 0, len(grid)
    col = len(grid[0])
    for r in range(0, rows):
        for c in range(0, col):
            if grid[r][c] == '@':
                neighbourrolls = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= r + i < rows and 0 <= c + j < col and grid[r + i][c + j] == '@':
                            if i == 0 and j == 0:
                                continue
                            neighbourrolls += 1
                if neighbourrolls < 4:
                    validrolls += 1
                    # Mark as pickable.
                    validrollindex.append([r,c])
    # Change the grid only after complete checking.
    for r, c in validrollindex:
        grid[r] = grid[r][:c] + 'x' + grid[r][c+1:]
    return validrolls

def main():
    if (len(sys.argv) != 2):
        print("Usage: python recursiverolls.py inputfile")
        return 1
    allvalidRolls = 0
    grid = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            grid.append(line.strip())
        prevgrid = grid
    allvalidRolls = allValidRollsIn(grid)
    print("Total valid rolls:", allvalidRolls)
    return 0

if __name__ == "__main__":
    main()
