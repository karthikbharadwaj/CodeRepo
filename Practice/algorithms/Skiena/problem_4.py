__author__ = 'karthikb'
s = {6, 13, 19, 3, 8}

from practice.general import merge_sort,binary_search

def solution_1():
    minv = float("+inf")
    maxv = float("-inf")

    for i in s:
        if i < minv: minv= i
        if i > maxv: maxv = i
    return maxv,minv

def colour_order(colour1,colour2):
    color_order = [red,blue,yellow]

def solution_4_3(a):
    a = [1,3,5,9]
    s = merge_sort(a)
    low = 0
    high = len(s)-1
    min_diff = float('inf')
    pairs = []
    while low < high:
        pairs.append((a[low],a[high]))
        low +=1
        high-=1
    print pairs

         




def solution_4_4():

   ''' Problem sort (number,color) pairs such that the colours are ordered
   '''
   a = [(1,'blue'), (3,'red'), (4,'blue'), (6,'yellow'), (9,'red')]
   total_len = len(a)
   red = []
   blue = []
   yellow = []
   for item in a:
       if item[1] == 'blue':
           blue.append(item)
       elif item[1] == 'red':
           red.append(item)
       else:
           yellow.append(item)
   return (red + blue + yellow)

def solution_4_5():
    ''' Algorithm to get mode of an array'''
    value_dict = {}
    a = [4,6,2,4,3,1]
    s= merge_sort(a)
    for item in s:
        value_dict[item] = value_dict.get(item,0) + 1
    max_key = 0
    max_value = 0
    for key,value in value_dict.iteritems():
        
        if value > max_value:
            max_key = key
            max_value = value
    return max_key

def solution_4_6(S1,S2,x):
    s2 = merge_sort(S2)
    low = 0
    for i in s1:
        if binary_search(s2,x-i,0,len(s2)):
            return (val,i)
    return -1:w



