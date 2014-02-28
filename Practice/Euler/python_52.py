__author__ = 'karthikb'


from general import get_digits
def sum_digits(n):

    return sum([int(c) for c in str(n)])


def solution():

    i =2

    while True:
        digits = set(get_digits(i))
        j = 2
        results = []
        while j <= 6:
            product = i*j
            #print product
            if digits == set(get_digits(product)):
                results.append(product)

            else:
                break
            j+=1
        if j == 6:
            return i,results
        #print "incrementing i",i
        i+=1







print solution()









