__author__ = 'karthikb'

a = {5, 6, 1, 2, 3, 4}

def get_subsets(a):
    ''' The function returns all possible subsets of a given set
    '''
    n = len(a)
    subsets = []
    for counter in range(2**n):

        subset = [a[j] for j in range(n) if counter &(1<<j)]
        subsets.append(subset)

    return subsets


#a = [5, 6, 7, 1, 2, 3, 4]
a = [2, 1]
a = [1, 2, 3, 4]
a = [1, 2, 3, 4, 5, 6, 7]

def findMin(a):
    ''' The function returns the min element of a sorted array
    awesome recursion
    '''
    return

def fibonacci(n):
    ''' Recursive fibo
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print fibonacci(6)

def iter_fibonacci(n):

    a,b=0,1

    if n == 1:
        return 1
    if n == 0:
        return 0
    i = 2
    while i <= n:
        c = a+b
        a,b=b,c
        i+=1
    return c


a = [[1, 2, 3], [4, 5, 6]]

def robot_movement(i,j,m,n,paths):



    if i==m:
        for k in range(j,n+1):
            paths.append((i,k))

        print paths
        return

    if j==n:
        for k in range(i,m+1):

            paths.append((k,j))

        print paths
    paths.append((i,j))
    robot_movement(i+1,j,m,n,paths)
    robot_movement(i,j+1,m,n,paths)
    return

def parathesis_printing(left,right,s,count):
    '''
    '''



    if left < 0 or right < left:
        print "invalid"
        return

    if left == 0 and right == 0:
        print s
    else:
        if left > 0:
            s += '('
            parathesis_printing(left-1, right, s, count+1)
        if right > left:
            s += ')'
            parathesis_printing(left, right-1, s, count+1)


parathesis_printing(2,2,'',0)























#def iter_fib(n):








