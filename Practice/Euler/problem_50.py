__author__ = 'karthikb'

from general import get_primes



def solution(n):
    ''' consecutive prime sum to a prime below n
    '''
    primes = get_primes(n)
    prime_set = set(primes)
    total = 0
    total_primes = len(primes)
    max_prime,max_count = 2,0
    cum_prime_sum = []


    for i in primes:
        total += i
        cum_prime_sum.append(total)


    for index,i in enumerate(primes):
        count = 0
        for j in range(index,total_primes):
            if cum_prime_sum[j] in prime_set and cum_prime_sum[j] > max_prime:
                count+=1
                max_prime = cum_prime_sum[j]
    return max_prime,max_count

print solution(100)
