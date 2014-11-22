__author__ = 'karthikb'
'''
The program finds the minimumCoins to attain Sum
using a coin stack
'''

def minCoinSum(coins,S):
    minCoins = {0:0}
    for i in range(1,S+1):
        for j in range(len(coins)):
            if i >= coins[j] and minCoins[i- coins[j]] + 1 < minCoins.get(i,float('inf')):
                minCoins[i] = minCoins[i- coins[j]] + 1
    return minCoins[S]
print minCoinSum([1,3,5],11)


