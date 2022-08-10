import sys

input=sys.stdin.readline

m,n=map(int,input().split())

graph=[list(map(int,input().split())) for _ in range(m)]
visited=[[-1]*n for _ in range(m)]

direction=[(0,-1),(0,1),(-1,0),(1,0)]

def dp(visited,graph,m,n,p,q):
    if p==m-1 and q==n-1:
        visited[p][q]=1
        return
    if visited[p][q]!=-1:
        return
    visited[p][q]=0
    for ddp,dq in direction:
        np=p+ddp
        nq=q+dq
        if 0<=np<m and 0<=nq<n:
            if graph[p][q]>graph[np][nq]:
                dp(visited,graph,m,n,np,nq)
                visited[p][q]+=visited[np][nq]
dp(visited,graph,m,n,0,0)
print(visited[0][0])