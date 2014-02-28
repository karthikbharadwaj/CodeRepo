__author__ = 'karthikb'

'''
Rearrange the negative and possitive numbers alternatively
a = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
solution = [9, -7, 8, -3, 5, -1, 2, 4, 6]
'''

def solution(a):

    stack = []
    output = []
    for i in a:

        if i > 0:
            stack.append(i)
        else:
            output.append(stack.pop())
            output.append(i)

