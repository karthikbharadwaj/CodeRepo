
'''
largest n digit pandigital prime
'''
from general import rotate,get_primes,is_prime,permute



def solution():
    s = "123456789"
    max_pan_digit = 0
    
    for i in range(9,4,-1):
        for num in permute(s[:i]):
                num = int(num)
                if num > max_pan_digit and is_prime(num):
                    max_pan_digit = num
        print "done with:",i,"max so far:",max_pan_digit
    return max_pan_digit
    

print solution()
