__author__ = 'karthikb'


def string_to_lst(s):
    s_array = [c for c in s]
    return s_array

def list_to_string(l):
    return ''.join([c for c in l])

def solution_1_1(s):
    '''
    determine if the string has all unique characters
    '''
    checker = 0
    for c in s:
        value = (ord(c) - ord('a'))
        if checker & (1<<value): return False
        checker |= 1<<value
    return True

def solution_1_2(s):
    '''
    reverse a string
    '''
    n = len(s)
    s_array = [c for c in s]
    mid = n //2
    print mid
    i = 0
    j = n-1
    while(i<mid and j>=mid):
        print i,j
        temp,s_array[i] = s_array[i],s_array[j]
        s_array[j]= temp
        i+= 1
        j-= 1
    return ''.join([c for c in s_array])


def solution_1_3(s):
    ''' remove duplicate character in string
    '''
    s = string_to_lst(s)
    m = len(s)
    tail = 1

    for i in range(1,m):
        for j in range(0,tail):
            if s[i] == s[j]:
                break
        if j==tail:
            s[tail]= s[i]
            tail+=1

    return list_to_string(s)



def solution_1_4(a,b):
    constant = 13
    value_dict = {}

    for c in a:
        if c is not '':

            value_dict[c] = value_dict.get(c,0)+ 1
    for c in b:
        if c is not '':
            value_dict[c] = value_dict.get(c,0)- 1
    print value_dict
    for v in value_dict.values():
        if v != 0: return False

    return True

def solution_1_5(s):
    s_list = string_to_lst(s)



    for index,c in enumerate(s_list):
        if c == ' ':
            s_list[index]='%20'
    return list_to_string(s_list)

a = [[0,1,2],[1,2,3],[3,4,5]]

def solution_1_7(a):
    index = []
    row = len(a)
    columns = 0

    for i in range(len(a)):
        for j in range(len(a)):
                if a[i][j]== 0:
                    index.append(i)
                    index.append(j)

    for i in range(len(a)):
        for j in range(len(a)):
            if i in index:
                a[i]= [0]
                a[:][i]= [0]
            if j in index:
                a[j][:] = [0]
                a[:][j] = [0]
    print a



#print solution_1_7(a)

def isSubstring(s1,s2):
    return s1 in s2

def solution_1_8(s1,s2):
    s3 = s1+s1
    print s3
    return isSubstring(s2,s3)

print solution_1_8('pleap','apple')


























