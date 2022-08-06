import sys

input=sys.stdin.readline

n,m=map(int,input().split())

array=list(map(int,input().split()))+[0]
mod=[0]*m
for i in range(n):
    array[i]+=array[i-1]
    mod[array[i]%m]+=1

cnt=mod[0]
for i in mod:
    cnt+=i*(i-1)//2
print(cnt)