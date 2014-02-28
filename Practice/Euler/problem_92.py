__author__ = 'karthikb'
'''
Problem Statement:

Finding out how many numbers below 10 million arrive at 89 in their number chain

A number chain is formed by summing up the squares of its digits. The chain ends in either 1 or 89
'''

from general import get_digits

number_chain_dt = {}
digits_sum_sq_dt = {}



def digits_sum_square(n):
    a = [0,1,4,9,16,25,36,49,64,81]

    return sum([a[n] for n in get_digits(n)])

def number_chain(n):
    #computing sum of square of digits
    # i = sum([i**2 for i in get_digits(i)])
    i = n
    number_set = set()
    while i not in number_set:
        if i in number_chain_dt:
            number_set = number_set.union(number_chain_dt[i])
            return number_set,i

        number_set.add(i)
        i = digits_sum_square(i)
    return number_set,i

def solution(n):
    solution_set = set() 
    result = 0
    for i in range(n):
        if i in solution_set:
            continue
        number_set,last_value = number_chain(i)
        number_chain_dt[i] = number_set

        if last_value ==89:
            solution_set = solution_set.union(number_set)
    return len(solution_set)



print solution(1000000)





