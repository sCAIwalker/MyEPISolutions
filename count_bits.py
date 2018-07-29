from test_framework import generic_test


#O(n) Time, O(1) Space
def count_bits(x):
    numBits = 0

    while x:
        numBits = numBits + (x & 1)
        x = x >> 1

    return numBits


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("count_bits.py", 'count_bits.tsv',
                                       count_bits))
