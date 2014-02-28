'''
If S is an infinite sequence of integers
f(n) indicates the starting position of nth occurrence of n
find summation(f(3**k)) for 1 <= k <=13
'''

def generate_ints(n):
    ''' The function generates a string as a sequence 
    of integers
    '''
    return ''.join([str(i) for i in range(n)])
s = generate_ints(120)

def solution(n):

    index = 0
    s = ''
    element = str(n)
    start_element = 0
    result = 0

    while n >0:
        index = s.find(element)
        if index <> -1:
            result +=index
            result +=1 
            s = ''
            n -=1
        start_element +=1
        s += str(start_element)
    return result

print solution(7780)


