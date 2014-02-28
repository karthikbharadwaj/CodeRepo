__author__ = 'karthikb'


from general import check_pandigital


def get_concat_product(num,n):
    product = ''.join([str(num*j) for j in range(1,n+1)])
    return product

def solution():

    solution_set = []
    concat_prod = str(52)+str(100)+str(52*100)
    print len(concat_prod),concat_prod

print solution()

