__author__ = 'karthikb'

'''
Stable Marriage Problem
M men and N women have a list of preferential order of partners
The SMP comes up with suitable matches such that the priorities are not violated
'''

M = ['m1', 'm2']
W = ['w1', 'w2']

choices = {'w1': ['m1', 'm2'], 'w2': ['m1', 'm2'], 'm1':['w1', 'w2'], 'm2':['w1', 'w2']}

def is_available(m, w, pairs):

   match_found = False
   if w in pairs:

       choice = choices[w]
       if choice.index(m) < choice.index(pairs[w]):
           pairs[w] = m
           match_found = True
   else:
       pairs[w] = m
       match_found = True
   return match_found

def solution(M, W, choices):
    pairs = {}

    for m in M:
        for w in choices[m]:
            if is_available(m,w,pairs):
                break


    return pairs

print solution(M, W, choices)
