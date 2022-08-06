import sys

s=input().strip()
q=int(input())
prefix_sum=[]
for _ in range(q):
    sum=0
    prefix_sum.clear()
    find,start,end=input().strip().split()
    start,end=int(start),int(end)

    if not prefix_sum:
        for i in s:
            if i==find:
                sum+=1
                prefix_sum.append(sum)
            else:
                prefix_sum.append(sum)
    if prefix_sum:
        if start:# start가 0이 아닐때
            print(prefix_sum[end]-prefix_sum[start-1])
        else:
            print(prefix_sum[end])
