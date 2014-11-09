__author__ = 'karthikb'

def stringtoList(s):
    return [c for c in s]

def checkPalindrome(s):
    print s
    length = len(s)
    moves = 0
    if length == 1:
        return moves
    mid = length /2
    i,j= 0,length -1
    while i < j:
        if s[i] != s[j]:
            diff = (ord(s[j]) - ord(s[i]))
            diff = diff if diff > 0 else -diff
            if diff < 25:
                moves += diff
            else:
                return 0
        i += 1
        j -= 1
    return moves

print checkPalindrome('hmhcy')
'''
5
feazhaxpux
hmhcy
tmp
11
11
58
27
4
'''
#abc
#abcba
#abcd
