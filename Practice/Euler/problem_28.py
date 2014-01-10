__author__ = 'karthikb'

def solution(n):
    i = 1
    summation = 0
    increment = 2
    count = 0
    while i < n**2:
        count+=1
        summation += i
        i += increment

        if count == 4:
            count = 0
            increment += 2

    return summation+i





print solution(1001)






