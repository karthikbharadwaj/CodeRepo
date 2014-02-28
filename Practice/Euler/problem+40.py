__author__ = 'karthikb'

def gen_irrational(n):
    return ''.join([ str(i) for i in range(1,n+1)])

def solution():
    '''
    Decimal number formed by concatenating integers
    0.123456789101112131415161718192021
    d12 = 1
    find d1 * d10 * d100 * d100 * d1000 * d10000 * d100000 * d1000000
    '''
    n = 1000000
    num = gen_irrational(n)
    values = reduce(lambda x,y: x*y,[int(num[10**i-1]) for i in range(7)])

    return values

print solution()






