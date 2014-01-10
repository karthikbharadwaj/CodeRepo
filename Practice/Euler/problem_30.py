__author__ = 'karthikb'


def solution():
    solution_set = []
    for i in range(1000,100000):
        summation = 0
        value = i
        #print value
        while value>=1:
            r = (value%10)
            summation+= r**5
            value = value //10
            if summation > i:
                continue
        if summation == i:
            solution_set.append(i)

    return sum(solution_set)


print solution()