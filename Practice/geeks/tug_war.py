from practice.euler import general
'''
The problem: Tug of War

Divide the array into two sets with minimum difference

Problem : Given {3, 4, 5, -3, 100, 1, 89, 54, 23, 20}
Expected output {4, 100, 1, 23, 20} and {3, 5, -3, 89, 54}
'''

def tug_war(a):

    s = general.merge_sort(a)
    first_array = []
    second_array = []
    i = 0
    total_len = len(s)
    print s
    while i <= total_len - 2: 

        print s[i],s[i+1]
        first_array.append(s[i])
        second_array.append(s[i+1])
        i += 2
    return first_array,second_array
a = [3, 4, 5, -3, 100, 1, 89, 54, 23, 20]
print tug_war(a)
