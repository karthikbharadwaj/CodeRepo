__author__ = 'karthikb'

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        pos_ref = {}
        #adding the array into dictionary
        for index, i in enumerate(num):
            pos_ref.setdefault(i,[]).append(index + 1)
        #sorting the array
        sorted_num = sorted(num)
        for item in sorted_num:
            index = self.binary_search(sorted_num,target-item)
            if index != -1:
                first_num = item
                second_num = target - item
                break
        if index == -1:
            return -1,-1
        elif first_num != second_num:
            first_index = pos_ref[first_num][0]
            second_index = pos_ref[second_num][0]
            if first_index < second_index:
                return first_index,second_index
            else:
                return second_index,first_index
        else:
            indexes = pos_ref[first_num]
            return indexes[0],indexes[1]

    def binary_search(self,a,key):

        i,j = 0,len(a)-1
        while i <= j:
            mid = i + (j - i)/2
            if (a[mid] == key):
                return mid
            elif a[mid] < key:
                i = mid + 1
            else:
                j = mid - 1
        return -1

s = Solution()
print s.twoSum([3,3,4],6)


