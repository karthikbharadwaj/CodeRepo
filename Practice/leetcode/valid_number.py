__author__ = 'karthikb'

class Solution:
    # @param s, a string h
    # @return a boolean
    def isNumber(self, s):
        ecounter = 0
        negcounter = 0
        dcounter = 0
        nums = self.get_words(s)
        if len(nums) != 1:
            return False
        num,length = nums[0],len(nums[0])
        accepted_symbols = ['0','1','2','3','4','5','6','7','8','9','e','.','-','+']
        remove_symbols = ['+','-','/','e',' ','.']
        if num:
            for i in range(0,length):
                if num[i] in accepted_symbols:
                    if num[i] == 'e':
                        if ecounter != 0 or self.validateExponent(i,num,length) == False:
                            return False
                        else:
                            ecounter += 1
                    elif num[i] == '.':
                        if dcounter != 0 or self.validateDecimal(i,num,length) == False:
                            return False
                        else:
                            dcounter += 1
                    elif num[i] == '-' or num[i] == '+':
                        if negcounter != 0 or self.validateNegative(i,num,length) == False:
                            return False
                        else:
                            negcounter += 1
                else:
                    return False
        else:
            return False
        return True

    def get_words(self,s):
        length = len(s)
        letterCount = 0
        words = []
        word = ''
        for i in range(0,length):
            if s[i] == ' ' and letterCount > 0:
                words.append(word)
                word = ''
                letterCount = 0
            elif s[i]!= ' ':
                word = word + s[i]
                letterCount += 1
        if word != '':
            words.append(word)
        return words

    def validateExponent(self,i,s,length):
        return (i-1 >= 0 and (s[i-1] == '.' or self.isNumber(s[i-1]))) and (i+1 < length and (self.isNumber(s[i+1])))

    def validateDecimal(self,i,s,length):
        return ((i + 1 < length and ((i !=0 and s[i+1]== 'e') or self.isNumber(s[i+1]))) or (i-1 >= 0 and self.isNumber(s[i-1])))

    def validateNegative(self,i,s,length):
        return ( i==0 and (i + 1 < length and self.isNumber(s[i+1:])))


s = Solution()

print s.isNumber(".e3")

