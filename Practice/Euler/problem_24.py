__author__ = 'karthikb'



def find_first(a):
    j = len(a) -1
    first_index = -1
    first_char = ''
    while j>0:

        if a[j] > a[j-1]:

            first_index,first_char = j-1,a[j-1]
            return first_index,first_char
        j -= 1
    return first_index,first_char

def find_second(a,first,first_index):
    second_char,second_index =  '',-1
    j = len(a) - 1
    for j in range(first_index,len(a)):

        if a[j] > first:
            second_index,second_char = j,a[j]
            return second_index,second_char
    return second_index,second_char

def replace_values(a,first_index,second_index):

    t = list(a)
    temp = t[second_index]
    t[second_index] = t[first_index]
    t[first_index] = temp
    return ''.join([i for i in t])


def lexical_permute():
    a = ['012']
    item = a[0]
    first_index = 0
    second_index = 0
    while first_index != -1 and second_index !=-1:
        first_index,first_char = find_first(item)
        print first_index,first_char
        second_index,second_char = find_second(item,first_char,first_index)
        print second_index,second_char
        new_item = replace_values(item,first_index,second_index)
        a.append(new_item)
        item = new_item
    print a

#lexical_permute()



first_index,first_char = find_first('012')
print first_index,first_char
second_index,second_char = find_second('012',first_char,first_index)













