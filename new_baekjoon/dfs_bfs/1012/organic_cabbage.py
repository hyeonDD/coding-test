import sys
from collections import deque

input=sys.stdin.readline

t=int(input())

direction=[(-1,0),(1,0),(0,-1),(0,1)]

def bfs(graph,x,y):
    q=deque()
    q.append((x,y))
    graph[x][y]=False

    while q:
        x,y=q.popleft()
        for nx,ny in direction:
            nx+=x
            ny+=y
            if nx>-1 and nx<n and ny>-1 and ny<m:
                if graph[nx][ny]:
                    graph[nx][ny]=False
                    q.append((nx,ny))

for _ in range(t):
    m,n,k=map(int,input().split())

    graph=[[False for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        a,b=map(int,input().split())
        graph[b][a]=True
    cnt=0

    for x in range(n):
        for y in range(m):
            if graph[x][y]:
                bfs(graph,x,y)
                cnt+=1

    print(cnt)