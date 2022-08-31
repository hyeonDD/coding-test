import sys
import heapq

INF=int(1e9)

input=sys.stdin.readline

v,e=map(int,input().split())

k=int(input())

graph=[[] for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

distance=[INF]*(v+1)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue

        for g in graph[now]:
            cost=dist+g[1]
            if cost<distance[g[0]]:
                distance[g[0]]=cost
                heapq.heappush(q,(cost,g[0]))

dijkstra(k)

for i in range(1,v+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])