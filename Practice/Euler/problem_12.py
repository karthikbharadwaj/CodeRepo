__author__ = 'karthikb'

from general import factors

def triangle_number(i):


    divisors = factors(i)
    if len(divisors) >= 500 and i == sum(divisors):
        return i
    else:
        triangle_number(i*3)


print triangle_number(1)











