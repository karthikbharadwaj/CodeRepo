s = '1232321111192323332777779'
mid = len(s)//2

def weighted_sum(n):
    total_len= len(n)
    w_sum = 0
    total_sum = 0

    for pos,i in enumerate(n):
        w_sum +=(pos+1)*int(i)
        total_sum += int(i)
    if total_len//2 == w_sum//total_sum:
        return True
    return False




def generate_sub_strings(s):
    sub_strings = {}
    chunk_size = 1
    while( chunk_size <=len(s)):
        for i in range(len(s)):
            value = s[i:chunk_size]
            if len(value)>= 1:
                sub_strings.setdefault(len(value),[]).append(value)
        chunk_size += 1

    return sub_strings

def reverse(s):
    txt = []
    for i in range(len(s)-1, -1, -1):
        txt.append(s[i])
    return ''.join(txt)

def check(key,values):
    for i in range(len(values)):
        for j in range(1,len(values)):
            first,second = values[i],reverse(values[j])
            if weighted_sum(first+second) == True:
                    print s.find(first),s.find(values[j]),len(values[i])
                    return True



    return False






def get_stave(sub_strings):

    keys = sub_strings.keys()[::-1]

    for key in keys:
        if check(key,sub_strings[key]):
                return

    return

sub_strings = generate_sub_strings(s)
get_stave(sub_strings)









