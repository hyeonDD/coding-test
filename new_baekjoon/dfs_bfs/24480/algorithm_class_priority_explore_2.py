import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

n,m,r=map(int,input().split())

graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)

for _ in range(1,m+1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt=1
def dfs(v):
    global cnt
    if not visited[v]:
        visited[v]=cnt
        
        graph[v]=reversed(sorted(graph[v]))

        for i in graph[v]:
            if not visited[i]:
                cnt+=1
                dfs(i)

dfs(r)

for i in range(1,n+1):
    print(visited[i])