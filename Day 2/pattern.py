# Sum of all invalid numbers in the range is the answer.
import sys

'''
    Invalid if:
    number is made up of a sequence of digits repeated twice.
    445445 - Invalid, 44 - Invalid but, 44544 - Valid.
    ID starts with 0.
'''
def findInvalids(r):
    sum = 0
    start, end = map(int, r.split('-'))
    for n in range(start, end + 1):
        if isInvalid(str(n)):
            sum += n
    return sum

def isInvalid(n):
    l = len(n)
    # IDs don't start with 0.
    if n[0] == '0':
        return True
    # len is even in the case of invalid cases. 2 * k = even.
    elif l % 2 != 0:
        return False

    # An invalid ID is made up of two equal halfs.
    # If multiplying the first half twice gives the number itself, the it's invalid.
    if (n[0:l//2] * 2 == n):
        return True
    return False

def main():
    if len(sys.argv) != 2:
        return 1
    invalidSum = 0
    with open(sys.argv[1], "r") as file:
        for line in file:
            rangeList = line.split(',')
        for r in rangeList:
            invalidSum += findInvalids(r)
    print(invalidSum)
    return 0

if __name__ == "__main__":
    main()
