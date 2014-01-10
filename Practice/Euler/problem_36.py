__author__ = 'karthikb'



from general import palindrome,binary_rep




def palidnromes_bases():

    summation = 0

    for i in range(1000000):

        if palindrome(str(i)) and palindrome(str("{0:b}".format(i))):
            summation += i

    return summation


print palidnromes_bases()
