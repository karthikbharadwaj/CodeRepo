__author__ = 'karthikb'

'''
Counting Sort
a = [1, 4, 1, 2, 7, 5, 2]
'''


def counting_sort(array, maxval):
    """in-place counting sort"""
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return (array,count)

print counting_sort( [1, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1], 7 )
#            prints: [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 7],[0, 4, 4, 2, 2, 0, 0, 1]
