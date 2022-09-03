import sys

INF=int(1e9)

input=sys.stdin.readline

n,m=map(int,input().split())

graph=[]
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph.append((a,b,c))

def bellman_ford(start):
    distance[start]=0
    for i in range(n):
        for j in range(m):
            now=graph[j][0]
            n_node=graph[j][1]
            n_cost=graph[j][2]
            if distance[now]!=INF and n_cost+distance[now]<distance[n_node]:
                distance[n_node]=n_cost+distance[now]
                if i == n-1:
                    return True
    return False


if bellman_ford(1):
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i]== INF:
            print(-1)
        else:
            print(distance[i])