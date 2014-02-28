__author__ = 'karthikb'

'''
problem_15 project Euler
'''


def build_array(m,n):
    return [[0]*n]*m

data_dict = {}

def robot_movement(i,j,m,n,count):
    
    if (i,j) in data_dict:

        return data_dict[(i,j)]

    if i == m:
        for k in range(j,n):
            robot_movement(i,k+1,m,n,count)
        count+=1

        return count

    if j == n:
        for k in range(i,m):
            robot_movement(k+1,j,m,n,count)
        count+=1
        return count
    
    data_dict[(i,j)] = robot_movement(i+1,j,m,n,count)+robot_movement(i,j+1,m,n,count)

    return data_dict[(i,j)] 

def build_neighbours(matrix,m,n):
    
    neighbours = {} 
    for row in range(m+1):
        for column in range(n+1):
            if row <= m-1 and column <= n-1:
                neighbours[(row,column)] = [(row+1,column),(row,column+1)]
            elif column <= n-1:
                neighbours[(row,column)] = [(row,column+1)]
            elif row <= m-1:
                neighbours[(row,column)] = [(row+1,column)]
    
    return neighbours

def get_paths(neighbours,matrix,m,n,start,end):
    
    queue = []
    queue.append(start)
    visited = set()
    path = [start]
    paths = []

    while queue:
        element = queue.pop(0)
        visited.add(element)
        nearby = neighbours.get(element)
        if nearby:
            for neighbour in neighbours.get(element):
                if neighbour not in visited:
                    queue.append(neighbour)
                    path += [neighbour]

                if neighbour== end:
                    paths.append(path)

    return len(paths)
#print robot_movement(0,0,20,20,0)
m = n = 15
start = (0,0)
end = (15,15)

matrix = build_array(m,n)
neighbours = build_neighbours(matrix,m,n)
import time
start_time  = time.clock()
#print get_paths(neighbours,matrix,m,n,start,end)
#print "First",time.clock() - start_time
start_time  = time.clock()
print robot_movement(0,0,20,20,0)
print "Second",time.clock() - start_time

