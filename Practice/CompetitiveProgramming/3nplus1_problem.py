

'''
The next number to n in the sequence is decided by : If n is odd then 3n + 1 else 2n
Given two integers i and j print the maximum cycle length of integer
'''

#from __future__ import print_function
import sys

data = sys.stdin.readline()

input = [int(value) for value in data.strip().split(' ')]

cache = {}

def sequence_gen(n):
    '''
    Sequence generator with cache

    :param n: Beginning number of sequence
    :return: Length of sequence
    '''

    if n in cache:
        return cache[n]
    elif n == 1:
        return 1
    elif n % 2 == 0:
        cache[n] = 1 + sequence_gen(n/2)
    else:
        cache[n] = 1 + sequence_gen(3 * n + 1)
    return cache[n]



max_value = -99999
for v in range(input[0],input[1]+1):
    max_value = max(max_value,sequence_gen(v))
print(input[0],input[1],max_value)


