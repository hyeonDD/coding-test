import sys
input=sys.stdin.readline
n,c=map(int,input().split())
homes=sorted([int(input()) for _ in range(n)])
start,end=1,homes[-1]-homes[0]
answer=0
while start<=end:
    mid=(start+end)//2
    current = homes[0]
    cnt = 1
    for i in range(1, len(homes)):
        if homes[i] >= current + mid:
            cnt += 1
            current = homes[i]    
    if cnt>=c:
        start=mid+1
        answer=mid
    else:
        end=mid-1
print(answer)

"""
5 3
1
2
8
4
9
"""