__author__ = 'karthikb'


a = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]

a1 = [20, 25, 1, 3, 4, 5, 7, 10, 14, 15, 16, 19]

a2 = [1,2,3,4]


def special_binary(a,left,right):

    mid = (right + left) //2



    print a[low:right]

    if a[left] < a[right]:

        return a[left]

    elif a[mid - 1] >= a[mid] and a[right] > a[mid]:
        return a[mid]
    elif a[low] > a[mid]:
        return special_binary(a,left, mid)


#print special_binary(a2, 0, len(a2) - 1)

def find_binary(a,left,right,key):

    mid =  left + (right - left) / 2

    print a[mid]
    if a[mid] == key:

        return mid

    elif a[left] >= a[mid]:

        if key < a[mid] and key > a[left]:

            return find_binary(a,left,mid - 1, key)
        else:

            return find_binary(a,mid + 1,right, key)

    elif a[right] > a[mid] and key > a[mid]:

        return find_binary(a,mid + 1,right, key)

    elif key < a[mid]:


        return find_binary(a,left,mid - 1, key)
    else:
        return -1
print find_binary([1,2,3,4], 0 , len([1,2,3,4])-1 , 2)
