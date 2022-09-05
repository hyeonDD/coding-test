import sys

input=sys.stdin.readline

n,s=map(int,input().split())

arr=[*map(int,input().split())]

left,right=0,0

answer,total=999999,arr[0]

while True:
    if total<s:
        right+=1
        if right==n:
            break
        total+=arr[right]
    else:
        total-=arr[left]
        answer=min(answer,right-left+1)
        left+=1

print(answer if answer!=999999 else 0)