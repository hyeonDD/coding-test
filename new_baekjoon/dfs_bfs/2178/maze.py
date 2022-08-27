import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split())

graph=[[*map(int,input().rstrip())] for _ in range(n)]

direction=[(-1,0),(1,0),(0,-1),(0,1)]

def bfs(graph,x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for nx,ny in direction:
            nx+=x
            ny+=y
            if nx>-1 and nx<n and ny>-1 and ny<m:
                if graph[nx][ny]==1:
                    graph[nx][ny]=graph[x][y]+1
                    q.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(graph,0,0))