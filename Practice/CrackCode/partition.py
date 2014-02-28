__author__ = 'Karthik'



def swap(a,b):
    return b,a

def lomuto_partition(a):
    left = 0
    right = len(a)
    p = a[left]
    index = left
    for i in range(1,right):
        if a[i]< p:
            index = index + 1

            a[index],a[i] = swap(a[index],a[i])

    a[index],a[left]=swap(a[index],a[left])

    return index

#print lomuto_partition([1,3,4,2,8])


def merge(b,c,a):
    k=0
    i=0
    j=0
    print b,c
    while i < len(b) and j < len(c):
        print i,j
        if b[i] < c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1

        k += 1
    if j==len(c):

       a[k:]= b[i:]

    else:
        a[k:] = c[j:]

    return a

def  merge_sort(a):
    n = len(a)
    if n > 1:
        mid = n/2
        b = a[:mid]
        #print b
        c = a[mid:]
        #print c
        merge_sort(b)

        merge_sort(c)

        return merge(b,c,a)



def longest_sub_string(s):

    n = len(s)
    start_index = 0
    max_run_length = 1


    for i in range(len(s)):
        run_length = 1
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                run_length += 1

            else:
                break


        if max_run_length < run_length:
            print "run length"
            max_run_length = run_length
            value = s[i:i+run_length]


        i = i + run_length

    return value

def factor(n):
    k = 1
    while k*k<n:
        if n%k == 0:
            yield k
            yield n//k
        k += 1
    if k * k == n:
        yield k


def msum2(a):
    bounds, s, t, j = (0,0), -float('infinity'), 0, 0

    for i in range(len(a)):
		t = t + a[i]
		if t > s: bounds, s = (j, i+1), t
		if t < 0: t, j = 0, i+1

    return (s, bounds)

#print msum2([1, 2, -5, 4, 7, -2])

def compute_power(x,y):
    if y == 0:
        return 1
    else:
        print "y//2",y//2
        value = compute_power(x,y//2)

        result = value * value
        if y %2==1:
            result *= x

        return result



def partition(a):
    n = len(a)
    i = 0
    pivot = a[i]
    index = i

    for j in range(1,len(a)):

        if a[j]< pivot:

            index = index + 1
            a[index],a[j] = swap(a[index],a[j])

    a[index], a[i] = swap(a[index], a[i])
    print a
    return index

print partition([4,5,2,3,1])
def hoarse_partition(a):

    left = 0
    right= len(a)-1
    pivot = a[left]

    while(left < right):

        while a[left]< pivot:
            left+=1
        while a[right] > pivot:
            right -= 1
        a[left],a[right] = swap(a[left],a[right])
    a[left],a[right] = swap(a[left],a[right])























def heap_bottomup(a):

    n = len(a)
    for i in range(n/2,1):
        k=i
        v= a[k]
        j=2*k
        heap = False
        while not heap and j<n:
            if a[j]<a[j+1]:
                j = j+1
            if v >= a[j]:
                heap = True
            else:
                a[k] = a[j]
                k = j
        a[k] = j











