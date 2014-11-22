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
            print diff,s[i],s[j]
            diff = diff if diff > 0 else -diff
            moves = moves + diff
            if i == 4:
                break
            #moves = (moves + diff) % 26
        i += 1
        j -= 1
    return moves

print checkPalindrome('daixyfjncgjszcddttqdftxwxeczroduonuosdbwlmomorrknipsboqautalhfixuclnholtccfrtzdihsakhrmbkopttxqobddir')

