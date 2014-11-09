__author__ = 'karthikb'

import csv
import re
import operator
class Solution:

    def read_file_to_dict(self,file):

        brands = {}
        f = open(file,'rb')
        for line in f:
            items = line.replace("[",'').replace("\"",'').replace("]",'').strip().split(',')
            for item in items:
                brands[item] = brands.get(item,0) + 1
        sorted_brands = sorted(brands.items(),key= operator.itemgetter(1),reverse= True)
        print sorted_brands[:11]



            #print line
            #print re.sub(r'"\[*\]',line)
        '''
        for line in f:
            print line.strip('\"').rstrip('[]')
            #print line.replace("\"",'').strip('[').strip('/]')
        '''



s = Solution()
s.read_file_to_dict('top10_sample.csv')

