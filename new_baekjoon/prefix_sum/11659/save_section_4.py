import sys

input=sys.stdin.readline

n,m=map(int,input().split())
array=list(map(int,input().split()))

sum=0
prefix_sum=[0]

for i in array:
    sum+=i
    prefix_sum.append(sum)

for _ in range(m):
    i,j=map(int,input().split())
    print(prefix_sum[j]-prefix_sum[i-1])