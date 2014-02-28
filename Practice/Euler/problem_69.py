'''
problem 69:
Finding the Totient maximum
'''

from general import get_primes

def find_totient(n):
    primes = get_primes(n)
    totient = n
    for prime in primes:
        if n % prime ==0:
            totient *=(1- (1/prime))
    return totient
print find_totient(36)

    

