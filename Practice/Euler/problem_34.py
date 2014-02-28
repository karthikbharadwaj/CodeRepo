__author__ = 'karthikb'

from general import factorial,get_digits
def solution():

    ''' Find all curious numbers which are the sum of the factorial of its digits
    '''
    solution_set = []
    i = 10
    #value = sum([factorial(j) for j in get_digits(i)])

    while True:

        value = sum([factorial(j) for j in get_digits(i)])
        if i == value:
            print i,value
            solution_set.append(i)

        if i > 1000000:
            return sum(solution_set)

        i += 1





print solution()



