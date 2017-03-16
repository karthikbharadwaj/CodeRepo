'''
modified problem 1 for solution of problem 2
'''
with open('input.txt', 'r') as input:
    a, b = [int(x) for x in input.readline().split(' ')]
with open('output.txt', 'w') as output:
    output.write(str(a + b * b))
    output.write('\n')
