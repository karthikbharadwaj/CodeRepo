__author__ = 'karthikb'

from general import get_primes,rotate
def solution(n):
    ''' circular prime whose rotations are also prime
    '''
    primes = set(get_primes(n))
    print primes
    solution_set = set()
    for prime in primes:
        if rotate(prime).issubset(primes):
            solution_set.add(prime)
    return len(solution_set)


print solution(1000000)