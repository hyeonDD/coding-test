import math

m,n = map(int,input().split())

def is_prime_range(x):
    array = [True] * (x+1)

    for i in range(2,int(math.sqrt(x))+1):
        if array[i] == True:
            j = 2
            while i*j<=x:
                array[i*j] = False
                j+=1
    return [i for i in range(2,x+1) if array[i]]
print(*filter(lambda x: x>=m and x<=n, is_prime_range(n)))