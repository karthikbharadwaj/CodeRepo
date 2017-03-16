
'''
Problem Statement :https://courses.edx.org/courses/course-v1:ITMOx+I2CPx+1T2017/courseware/
5f7ded3dde75420f8da894830d69e7e4/05c1037ba1e2450e931dfbd1c2d1856d/
'''

with open('input.txt','r') as input:
    n = int(input.readline())
    p = [int(px) for px in input.readline().split(' ')]
    t = [int(tx) for tx in input.readline().split(' ')]


max_val = 0
max_index = 0
second_max_index = 0
max_dist = abs(p[0] - t[0])
sec_dist = max_dist

for i in range(1,n):
    dist = abs(p[i] - t[i])
    if dist >= max_dist:
        sec_dist = max_dist
        second_max_index = max_index
        max_dist = dist
        max_index = i

#print max_index,second_max_index

max_val = max(p[max_index] + t[second_max_index], p[second_max_index] + t[max_index])

for i in range(0,n):
    if i not in [max_index,second_max_index]:
        max_val += max(p[i],t[i])

with open('output.txt','w') as output:
    output.write(str(max_val))
    output.write('\n')















