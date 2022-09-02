import sys
import heapq

INF=int(1e9)

input=sys.stdin.readline

n,e=map(int,input().split())

if e==0:
    print(-1)
    sys.exit(0)

graph=[[] for _ in range(n+1)]

for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start,end):
    distance=[INF]*(n+1)
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        
        if distance[now]<dist:
            continue

        for n_node,n_cost in graph[now]:
            cost=dist+n_cost
            if cost<distance[n_node]:
                distance[n_node]=cost
                heapq.heappush(q,(cost,n_node))
    return distance[end]

x1,x2=map(int,input().split())

result=min((dijkstra(1,x1)+dijkstra(x1,x2)+dijkstra(x2,n)),(dijkstra(1,x2)+dijkstra(x2,x1)+dijkstra(x1,n)))
print(result if result<INF else -1)