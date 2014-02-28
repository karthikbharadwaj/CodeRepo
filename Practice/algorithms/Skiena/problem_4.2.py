__author__ = 'karthikb'
s = {6, 13, 19, 3, 8}

def solution_1():
    minv = float("+inf")
    maxv = float("-inf")

    for i in s:
        if i < minv: minv= i
        if i > maxv: maxv = i
    return maxv,minv




print solution_1()


def problem_
