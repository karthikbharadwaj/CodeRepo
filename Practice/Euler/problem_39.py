__author__ = 'karthikb'

def right_triangle(p):
    counter = 0
    for i in range(1,p+1):
        for j in range(1,i):
            for k in range(1,j):
                if i + j + k ==  p and k**2 + j**2 == i**2:
                    counter += 1
    return counter
max_value = 0
for i in range(1,1001):
    max_value = max(max_value,right_triangle(i))
print max_value



