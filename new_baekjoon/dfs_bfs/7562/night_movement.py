import sys
from collections import deque

input=sys.stdin.readline

t=int(input())

direction=[(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)]

def bfs(graph,x1,y1,x2,y2,n):
    q=deque()
    q.append((x1,y1))

    while q:
        if x1==x2 and y1==y2:
            break
        x,y=q.popleft()
        if graph[x2][y2]!=0:
            break
        for nx,ny in direction:
            nx+=x
            ny+=y
            if -1<nx<n and -1<ny<n and not graph[nx][ny]:
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))
    return graph[x2][y2]



for _ in range(t):
    n=int(input())

    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())

    graph=[[0]*n for _ in range(n)]
    print(bfs(graph,x1,y1,x2,y2,n))

"""
1
8
0 0
7 0

"""