import sys

input=sys.stdin.readline
INF=int(10e9)
n=int(input())
m=int(input())
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i]=0

for _ in range(m):
    a,b,c=map(int,input().split())
    if c<graph[a][b]:
        graph[a][b]=c

for k in range(1,n+1): # 거쳐가는 점이다
    for i in range(1,n+1): # 시작점
        for j in range(1,n+1): # 끝점
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
# 1,3(다이렉트)으로 가는것이 가장 짧은가 ? or 1,2(k) 2(k),3 을거쳐 가는것이 빠른가?

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF:
            print(0,end=' ')
        else:
            print(graph[i][j],end=' ')
    print()
