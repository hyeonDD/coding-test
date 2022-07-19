n=int(input())
result = [1]
def factorial(x):    
    if x==0:   
        return 1      
    else:
        result[0] = x*result[0]
        x=x-1
        factorial(x)
    return result[0]
print(factorial(n))