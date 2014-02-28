__author__ = 'karthikb'

'''
Truncatable primes
'''

from general import is_prime

def truncate_right(n):
    s = str(n)
    return [int(s[:i])for i in range(len(s),0,-1)]

def truncate_left(n):
    s = str(n)
    return [int(s[i:])for i in range(0,len(s))]


def check_primes(num_list):

    for item in num_list:
        if not is_prime(item):
            return False
    return True

def solution():
    solution_set = []
    count = 0
    i = 172080

    while count <= 11:
        print i
        if check_primes(truncate_right(i)) and check_primes(truncate_left(i)):
            count +=1
            solution_set.append(i)
            print i,count
            return i
        i += 1
    return sum(solution_set)

print solution()
