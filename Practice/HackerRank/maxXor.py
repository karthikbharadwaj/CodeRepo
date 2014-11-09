__author__ = 'karthikb'

def  maxXor( l,  r):
    maxxor = {}
    maxXor = -float('inf')
    value = 0
    for i in range(l,r+1):
        for j in range(1,r+1):
            if (i,j) in maxxor or (j,i) in maxxor:
               value = maxxor[(i,j)]
            else:
                value = i ^ j
                maxxor[(i,j)] = value
                maxxor[(j,i)] = value

            maxXor = max(maxXor,value)
    return maxXor

print maxXor(10,15)


