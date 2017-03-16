
'''
Create a team problem
Karthik
'''

from decimal import Decimal as D
from fractions import Fraction
import math

def get_small_matrix(data,k,n):
    small_matrix = []
    row = []
    y = D('2')
    for i in range(0,n):
        for j in range(0,n):
            if i!=k and j!=k:
                row.append(D(data[i][j]))
    return max(row[0]** y + row[3] ** y,row[1] ** y + row[2] ** y)
    #return max(math.pow(row[0],2) + pow(row[0],y) + pow(row[3],y) + pow(row[1],y) + pow(row[2],y))



def read_data(n):
    data = []
    for i in range(0,n):
        p = [int(px) for px in input.readline().split(' ')]
        data.append(p)
    return data

with open('input.txt','r') as input:
    data = read_data(n=3)


n = len(data)
y = D(2)
z = D(0.5)
team_efficiency = 0
for i in range(0,n):
    value = D.sqrt(D(pow(data[i][i],y)) + get_small_matrix(data,i,n))
    team_efficiency = max(team_efficiency,value)

with open('output.txt','w') as output:
    output.write(str(team_efficiency))
    output.write('\n')





















