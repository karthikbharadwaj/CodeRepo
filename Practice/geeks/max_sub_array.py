'''
Kadane's algorithm for maximum sum using dp
'''
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

#a = [-2,-3,4,-1,-2,1,5,-3]

'''

 F[i]  =  {  F[i-1] +  cij if  F[i-1 ] + cij >   F[i-1]
             F[i-1] otherwise
'''

def max_sub_array(a):

    f = {}
    max_so_far = max_ending_here = a[0]
    for i in range(1,len(a)):
        max_ending_here = max(0,max_ending_here * a[i])
        max_so_far = max(max_ending_here,max_so_far)
    return max_so_far

print max_sub_array(a)


