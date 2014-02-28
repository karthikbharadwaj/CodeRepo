'''
problem 11:
    Find the maximum product in the grid
'''

from general import factors
data_set = '..//Data//Euler//problem_11_data.txt'

def read_matrix_data(data_set):
    ''' The function read the matrix data'''
    data_set = open(data_set)
      
    return [[int(value) for value in row.split()] for row in data_set]

data = read_matrix_data(data_set)

def solution():
    ''' finding the maximum product'''
    max_product = -float("inf")
    total_rows = total_cols = len(data)
    tb_product = dg_product = lr_product = tu_product = 0
    for row in range(total_rows):
        for column in range(total_cols):
                
                #finding the max top and bottom
                if row <= total_rows -4:
                    tb_product = data[row][column] * data[row+1][column] * data[row+2][column] * data[row+3][column]

                #finding the max down diagonal 
                if row <= total_rows -4 and column <= total_cols-4:
                    dg_product = data[row][column] * data[row+1][column+1] * data[row+2][column+2] * data[row+3][column+3]

                #finding the max left and righ 
                if column <= total_cols -4:
                    lr_product = data[row][column] * data[row][column+1] * data[row][column+2] * data[row][column+3]
                #finding the max up diagonal
                if row >=4 and column <= total_cols-4:
                    tu_product = data[row][column] * data[row-1][column+1] * data[row-2][column+2] * data[row-3][column+3]
                
                max_product = max(max_product,tb_product,dg_product,lr_product,tu_product)

        
    return max_product
#print solution()
print factorial
