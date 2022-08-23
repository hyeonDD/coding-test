import sys

sys.setrecursionlimit(10**9)

input=sys.stdin.readline

n=int(input())
m=int(input())

graph=[[] for _ in range(n+1)]

for i in range(1,m+1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[0]*(n+1)

def dfs(v):
    visited[v]=1
    for g in graph[v]:
        if not visited[g]:
            dfs(g)

dfs(1)

print(sum(visited)-1)