
'''
Win Competition problem
'''

with open('input.txt','r') as input:
    n =  int(input.readline().strip())
    tval = [int(t)for t in input.readline().split(' ')]

max_sol = 0
count = 0
new_tval = sorted(tval)

for i in range(0,n):
    if max_sol + new_tval[i] <= 18000:
        max_sol += new_tval[i]
        count += 1



with open('output.txt','w') as output:
    output.write(str(count))
    output.write('\n')

