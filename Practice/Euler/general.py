__author__ = 'karthikb'

def palindrome(a):

    i = 0
    n = len(a) - 1
    j = n

    while i <= n//2 and j >= n//2:

        if a[i] != a[j]:
            #print a[i],a[j]
            return False
        i +=1
        j -=1
    return True

def binary_rep(a):
    s = ''
    while a >=1:
        r = str(a % 2)
        s = s.join(r)



        print r
        a = a //2
    return r




def factors(a):
    return [ i for i in range(1,a) if a % i == 0]

def power(a,b):

    if b == 1:
        return a

    value = power(a,b//2)
    output = value * value
    if b % 2 != 0:
        output = a * output

    return output

def permute(s):

    if len(s) == 1:
        return s
    permutations = []
    first = s[0]
    rest = s[1:]
    words = permute(rest)

    for word in words:
        for i in range(len(word)+1):
            permutations.append(word[:i]+first+word[i:])

    return permutations

def merge(a,b):
    c = []
    i = j = 0
    while i< len(a) and j < len(b):
        if a[i]> b[j]:
            c.append(b[j])
            j+=1
        else:
            c.append(a[i])
            i+=1

    if j == len(b):
        c.extend(a[i:])
    else:
        c.extend(b[j:])

    return c



def merge_sort(a):
    total_len = len(a)

    if total_len == 1:
        return a
    first = a[:total_len//2]
    second = a[total_len//2:]

    return merge(merge_sort(first),merge_sort(second))

#print permute('0123456789')








