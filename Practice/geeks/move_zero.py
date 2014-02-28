__author__ = 'karthikb'

'''
Problem: Move all zeros to the end of the array
a = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
solution = [1, 9 , 8, 4, 2, 7, 6, 9, 0, 0 , 0, 0]
'''

def solution(a):

    n = len(a)
    result = []
    count = 0
    for i in a:
        if i != 0:
            result.append(i)
            count += 1
    result += [0] * (n-count)
    return result

print solution([1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9])
