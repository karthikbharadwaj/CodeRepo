'''
Finding the longest increasing subsequence
'''


def lis(a):

    '''
    f[i] = longest increasing subsequence ending at element i
    '''

    result = []
    max_val = - float('inf')

    for i in range(len(a) - 1):

        if a[i] < a[i+1]:

            result.append(a[i])


    return result

a = [2, 6, 3, 4, 1, 2, 9, 5, 8]

print lis(a)
