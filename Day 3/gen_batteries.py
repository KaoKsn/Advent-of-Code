'''
    Find the largest 'size' digit number that can be formed from a given seq of digits.
    Example: 234234234234278 - seq, size - 12
                434234234278.

    Greedy Algorithm,
    Always find the largest number within an subseq.
    First iteration from 0 to len - size.
    ** Increment end by 1 everytime
    Break the loop once it reaches len, you have 'size' amount of digits.
    ** If seq[start + 1] remains the largest element, increment both start and prevIndex by 1.
    ** Else, change the largest digit to the value at the found index, and prevIndex to the absolute index value of the largest.
    Next iteration in start + 1, end + 1 < start has the index of the previous largest number found.
    largest for this iteration is seq[start + 1] i.e the first element in the subseq.
'''
import sys
def maxJolts(bank, size):
    maxJolt, size = '', int(size.strip())
    l = len(bank)
    start, end = -1, l - size

    if l < size:
        print("Invalid Size!")
        sys.exit(1)
    elif l == size:
        return int(bank)

    prevIndex = start
    while end < l:
        largest = bank[start + 1]
        for j, n in enumerate(bank[start+1:end + 1]):
            if int(n) > int(largest):
                largest = n
                # prevIndex - absolute index of the prev largest value found.
                prevIndex = j + 1 + start
        # If the index didn't change increment the indices by 1.
        if (start == prevIndex):
            start += 1
            prevIndex += 1
        else:
            start = prevIndex
        end += 1
        maxJolt += largest
    return int(maxJolt)

def main():
    if (len(sys.argv) != 3):
        print("Usage: python gen_batteries.py inputfile size")
        return
    max, size = 0, sys.argv[2]
    with open(sys.argv[1], "r") as file:
        for line in file:
            max += maxJolts(line.strip(), size)
    print("Max:", max)
    return 0

if __name__ == "__main__":
    main()
