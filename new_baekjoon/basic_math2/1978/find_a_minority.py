import math

n = int(input())
x = list(map(int,input().split()))

def is_prime(x):
    if x==1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

cnt=0
for i in x:
    if is_prime(i):        
        cnt+=1
print(cnt)