from itertools import combinations as b
n,m=map(int,input().split())
for i in b(range(1,n+1),m):
    print(*i)