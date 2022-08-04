import sys

n,k=map(int,input().split())

array=list(map(int,input().split()))

prefix_sum=[]

sum,cnt,idx=0,0,0
flag=False

for i in array:
    cnt+=1
    sum+=i
    if flag:
        sum-=array[idx]
        prefix_sum.append(sum)
        idx+=1
    if cnt>=k:
        prefix_sum.append(sum)
        flag=True

print(max(prefix_sum))