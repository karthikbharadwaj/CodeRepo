'''
Problem 32.py

Find the sum of all pandigitital products
Pandigitital product:
     Multiplier * multiplicant = product

All the three put together should be pandigital-n 
'''
from general import get_digits,check_pandigital

def solution():

    solution_set = set()
    visited = {}
    for i in range(10,10000):
        for j in range(10,10000):
            product = i * j
            value = str(i)+str(j)+str(product)
            #print value
            if check_pandigital(value,9) and product not in visited:
                visited[product] = 1
                print value
                solution_set.add(product)
    return sum(solution_set)
print solution()
#print check_pandigital(9876543212,9)
