__author__ = 'karthikb'

from math import sqrt,pow

factors = {}

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



def power(a,b):

    if b == 1:
        return a

    value = power(a,b//2)
    output = value * value
    if b % 2 != 0:
        output = a * output

    return output

def factorial(n):
    '''finding the factorial of n'''

    if n ==0:
        return 1
    if n == 1:
        return 1
    if n>1:
        return n*factorial(n-1)

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



def get_digits(n):
    ''' Given an number n the functino returns the digits as a list
    '''
    digits = []
    while n>=1:
        r = n % 10
        n //= 10
        digits.append(r)
    return digits

def string_to_lst(s):
    s_array = [c for c in s]
    return s_array


def get_primes(limit):
    '''Eratosthenes seive to generate prime numbers until n'''
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes


def check_pandigital(num,n):
    digits = [i for i in range(1,n+1)]
    if num is not int:
        num = int(num)
    try:
        #print get_digits(num)
        for i in get_digits(num):
            digits.remove(i)

        if len(digits)== 0:
            return True
    except:

        return False




def is_triangle(a,b,c):
    '''check if the three sides form a triangle'''

    return c**2 >= a**2+b**2 and a**2>=b**2+c**2 and b**2 >= a**2+c**2

from collections import deque

def rotate(num):
    num_string = str(num)
    digits = string_to_lst(num_string)
    total_len = len(digits)
    return {int(''.join(digits[i:]+digits[:i])) for i in range(total_len)}

def is_prime(n):
    '''  The function returns True if n is prime else False'''
    
    if n==1:
        return False
    
    if n ==2 or n==3:
        return True
    i = 2
    while i < n:
        if n%i == 0:
            return False
        i += 1
    return True

def factors(n):
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result

def binary_search(a,key,low,high):
    ''' 
    Binary Search key in a
    '''
    if low > high: return -1

    middle = (low + high)/2

    if a[middle] == key:

        return middle

    elif a[middle] > key:

        return binary_search(a,key,low,middle-1)

    else:

        return binary_search(a,key,middle+1,high)

