__author__ = 'karthikb'


class Solution_1:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if not a or not b:
            return a or b

        index = -1
        carry = 0
        result = []
        while -index <= max(len(a), len(b)):
            x = int(a[index]) if -index <= len(a) else 0
            y = int(b[index]) if -index <= len(b) else 0
            print "X value",x,"Y value:",y
            carry, remainder = divmod(x + y + carry, 2)
            result.append(remainder)
            index -= 1

        if carry:
            result.append(carry)

        return ''.join(map(str, reversed(result)))
s = Solution_1()
print s.addBinary('0','')
class Solution:
    def addBinary(self,a,b):
        if not a or not b:
            return a or b

        s,carry = '',0
        diff = len(a) - len(b)
        if diff > 0:
            b = diff * '0' + b
        else:
            a = -diff * '0' + a
        i = len(a)- 1
        while i >=0:
            print a[i]
            total = int(a[i]) + int(b[i]) + int(carry)
            print total
            value,carry = str(total//2),total % 2
            #value,carry = self.findSum(a[i],b[i],carry)
            i -= 1
            s = value + s
        if carry:
            s = carry + s
        return s


    def findSum(self,a,b,c):
        if a=='1' and b=='1' and c=='1':
            return '1','1'
        elif a =='1' and  b == '1':
            return '0','1'
        elif (a == '1' or b=='1') and c=='1':
            return '0','1'
        elif (a == '1' or b=='1'):
            return '1','0'
        elif c =='1':
            return '1','0'
        else:
            return '0','0'


s = Solution()
print s.addBinary('111','1')




