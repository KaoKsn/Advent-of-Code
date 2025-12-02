# Sum of all invalid numbers in the range is the answer.
import sys

'''
    Invalid if:
    number is made up of a sequence of digits repeated "atleast twice".
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
    if (l == 1):
        return False
    # IDs don't start with 0.
    if n[0] == '0':
        return True
    else:
        # n[0:l] * (l//l) would obviously be equal to the number itself.
        # So, iterate only till l - 1.
        for i in range(1, l):
            # Since we get invalid IDs in multiples of 5 starting from 2.
            if n[0:i]*(l // i) == n:
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
