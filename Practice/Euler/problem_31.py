'''
problem 31:
    What are all possible ways to get 2 pounds
'''


def solution(N):

    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    max_coins = {0:0,1:1}
    for S in range(1,N + 1):
        for i in range(0,len(coins)):
            if S>= coins[i]:
                max_coins[S] = max(max_coins.get(S,0),max_coins[S-coins[i]] + 1)
    return max_coins[N]

print solution(5)





