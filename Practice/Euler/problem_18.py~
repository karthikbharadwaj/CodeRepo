__author__ = 'karthikb'

triangle_file = open('C:\\CodeRepo\\practice\\Data\\Euler\\triangle_2.txt','r')


max_dict = {}


def solution(t_data):
    '''
    Solving using dp approach F(i,j) = max(F(i-1,j),F(i-1,j+1)) + cij
    '''

    F = {}

    total_rows =  len(t_data)
    print total_rows
    for i in range(total_rows):
        for j in range(i+1):
            F[(i,j)] = max(F.get((i-1,j),0),F.get((i-1,j-1),0)) + t_data[i][j]

    print max(F.values())
    #i= total_rows-1
    #print max([F.get((i,j),0) for j in range(total_rows-1)])



def read_triangle(triangle_file,n):
    ''' Read triangle data
    '''
    triangle_data = []
    #t_data = [line.split() for line in triangle_file]
    for line in triangle_file:
        #line.strip().split(' '):
        value = [int(value) for value in line.split()]
        zero_values = n - len(value)
        triangle_data.append(value +[0] * zero_values)
    return triangle_data

t_data = read_triangle(triangle_file,15)
solution(t_data)

