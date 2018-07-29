from test_framework import generic_test


#O(n) for a brute force by going through each bit, O(1) Space
# def parity(x):
#     numOnes = 0
#
#     while (x):
#         if ((x & 1) == 1):
#             numOnes += 1
#         x = x >> 1
#     return numOnes % 2

#O(k), let k be the number of bits set to 1 in a particular word. O(1) Space
def parity(x):
    result = 0
    while x:
        result = result ^ 1
        x = x & (x - 1)
    return result

#O(n/L) time complexity with caching where n is the word size(For example 64 bits)
#and L is the width of the key in bits (For example 16 bits)

#O(log n) solution where n is the word size by using XOR. We can combine caching and this approach
# def parity(x):
#     x = x ^ (x >> 32)
#     x = x ^ (x >> 16)
#     x = x ^ (x >> 8)
#     x = x ^ (x >> 4)
#     x = x ^ (x >> 2)
#     x = x ^ (x >> 1)
#     return x & 0x1


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
