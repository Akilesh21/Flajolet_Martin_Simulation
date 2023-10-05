
import math

def hashing(x):
    y = (3 * x + 1) % 5
    b = int(bin(y)[2:])
    return b

def trailing_zeros(x):
    if x == 0:
        return 1
    count = 0
    while x & 1 == 0:
        count += 1
        x >>= 1
    return count

def calculate_cardinality(value):
    max_zeroes = 0
    p = trailing_zeros(hashing(value))
    if max_zeroes < p:
        max_zeroes = p
    r = max_zeroes
    cardinality = 2**r
    return cardinality
