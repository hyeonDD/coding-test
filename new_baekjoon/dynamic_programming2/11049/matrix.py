import sys

n=int(input())

matrix=[list(map(int,input().split())) for _ in range(n)]

d=[[0]*n for _ in range(n)]

for i in range(1,n):
    for start in range(n-i):
        end= start+i
        result=float("inf")
        for cut in range(start,end):
            result = min(result,d[start][cut]+d[cut+1][end]+matrix[start][0]*matrix[cut][1]*matrix[end][1])
            d[start][end]=result
print(d[0][-1])




# abcd ab(cd) abc(d) a(bcd) 