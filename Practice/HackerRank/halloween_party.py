__author__ = 'karthikb'

class Solution:
    _max_slize = {2:1}
        #for i in range(n+1):
        #    input = raw_input()
        #    print self.get_max_slize(input)

    def get_max_slize(self,n):
        sol = 2
        count = 2
        if n <= 1:
            return 0
        elif n in self._max_slize:
            return self._max_slize[n]
        else:
            value = self.get_max_slize(n -1) + (n/2)
            self._max_slize[n] = value
            return value

    def iter_max_slize(self,n):
        if n <= 1:
            return 0

        elif n in self._max_slize:
            return self._max_slize[n]
        else:
            count = 3
            for i in range(n+1):
                self._max_slize[count] = self._max_slize[count-1] + count/2
                count += 1
        return self._max_slize[n]

s = Solution()
#print s.get_max_slize(10000000)
print s.iter_max_slize(7)



