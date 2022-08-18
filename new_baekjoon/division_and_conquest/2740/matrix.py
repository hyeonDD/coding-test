import sys
n,m=map(int,sys.stdin.readline().split())
matrix1=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
 
_,mk=map(int,sys.stdin.readline().split())
matrix2=[list(map(int,sys.stdin.readline().split())) for _ in range(m)]
 
 
result=[]
tmp=0
tmp_li=[]
for i in range(n):
    for j in range(mk):
        for k in range(m):
            tmp+=matrix1[i][k]*matrix2[k][j]
        tmp_li.append(tmp)
        tmp=0
    result.append(tmp_li)
    tmp_li=[]
 
for li in result:
    print(*li)