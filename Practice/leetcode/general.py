__author__ = 'karthikb'


def binary_search(a,key):

    i,j = 0,len(a)-1
    while i <= j:
        mid = i + (j - i)/2
        if (a[mid] == key):
            return mid
        elif a[mid] < key:
            i = mid + 1
        else:
            j = mid - 1
    return -1

def get_words(s):
    length = len(s)
    letterCount = 0
    words = []
    word = ''
    for i in range(0,length):
        if s[i] == ' ' and letterCount > 0:
            words.append(word)
            word = ''
            letterCount = 0
        elif s[i]!= ' ':
            word = word + s[i]
            print word
            letterCount += 1
    if word != '':
        words.append(word)
    return words



if __name__ == "__main__":
    #s = binary_search([3,4,5,6],3)
    print get_words('abc ab  c')
    a = {}

