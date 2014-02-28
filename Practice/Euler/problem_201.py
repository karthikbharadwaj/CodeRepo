'''
Problem 201:  Unique sum of subsets of a Set
'''

a = [1,3,6,8,10,11]

def generate_subsets(a):
    ''' The function generates subsets of a set'''
    n = len(a)
    subsets = []
    for i in range(2**n):
        subset = set()
        for j in range(n):
            if i & j:
                subset.add(a[j])
        print subset        
    return subsets
    

print generate_subsets(a)
