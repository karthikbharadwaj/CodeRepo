__author__ = 'karthikb'



def generated_fibo(max_range):
    fibo = {0:0,1:1}
    i = 2
    while i <= max_range:
        fibo[i] = fibo[i-1] + fibo[i-2]
        i += 1
    return fibo

def is_fibo(N,fibo):
    if N in fibo:
        return "IsFibo"
    return "IsNotFibo"

fibo = generated_fibo(10**10)



