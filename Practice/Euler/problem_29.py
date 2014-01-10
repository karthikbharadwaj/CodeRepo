__author__ = 'karthikb'

power_dict = {}

def power(a,b):

    if b == 1:
        return a

    if (a,b) in power_dict:
        return power_dict[(a,b)]

    value = power(a,b//2)
    output = value * value
    if b % 2 != 0:
        output = a * output

    return output


power_dict = {}
def compute_power(a,b):
    if (a,b) in power_dict:
        return power_dict[(a,b)]
    else:
        return pow(a,b)

def distinct_sequence():
    return len({compute_power(i,j) for i in range(2,101) for j in range(2,101)})


print distinct_sequence()





