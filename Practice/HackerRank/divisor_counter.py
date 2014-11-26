__author__ = 'karthikb'

def count_divisor(N):
    divident = N
    counter = 0
    while N >0:
        divisor = N % 10
        if divident % divisor == 0:
            counter += 1
        N = N / 10
    return counter

print count_divisor(122)
