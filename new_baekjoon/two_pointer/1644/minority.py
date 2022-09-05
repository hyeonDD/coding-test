import sys
import math

input=sys.stdin.readline

n=int(input())

if n==1:
    print(0)
    sys.exit(0)
elif n==2:
    print(1)
    sys.exit(0)

def is_prime_range(n):
    arr=[True]*(n+1)

    for i in range(2,int(math.sqrt(n))+1):
        if arr[i]:
            j=2
            while i*j<=n:
                arr[i*j]=False
                j+=1
    return [i for i in range(2,n+1) if arr[i]]

arr=is_prime_range(n)
len_arr=len(arr)
    
left,right=0,1

total=arr[0]
answer=0

while True:
    if total<n:
        total+=arr[right]
        if total==n:
            answer+=1
        right+=1
    else:
        total-=arr[left]
        if total==n:
            answer+=1
        left+=1
        if left==len_arr-1:
            break
print(answer)