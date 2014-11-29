__author__ = 'karthikb'



def generated_fibo(max_range):
    fibo = {0:0,1:1}
    series ={0:1,1:1}
    i = 2
    while True:
        fibo[i] = fibo[i-1] + fibo[i-2]
        series[fibo[i]] = 1
        if fibo[i]>=max_range:
            break
        i += 1
    return series

def is_fibo(N,fibo):
    if N in fibo:
        return "IsFibo"
    return "IsNotFibo"

series = generated_fibo(10**10)

print is_fibo(7,series)



