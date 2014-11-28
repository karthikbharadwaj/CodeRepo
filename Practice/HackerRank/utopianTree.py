__author__ = 'karthikb'

def utopianTree(n):
    T = {0:1}
    return _utopianTree(n,T)

def _utopianTree(N,T):
    if N in T:
        return T[N]
    elif N % 2 == 0:
        T[N] = _utopianTree(N-1,T) + 1
    else:
        T[N] = _utopianTree(N-1,T) * 2
    return T[N]

print utopianTree(60)

