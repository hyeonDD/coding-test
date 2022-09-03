import sys
import heapq

INF=int(1e9)

input=sys.stdin.readline

T=int(input())

def dijkstra(start,end):
    q=[]
    distance=[INF]*(n+1)
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)

        if dist<distance[now]:
            continue

        for n_cost,n_node in graph[now]:
            cost=dist+n_cost
            if cost<distance[n_node]:
                distance[n_node]=cost
                heapq.heappush(q,(cost,n_node))
    return distance[end]

for _ in range(T):
    n,m,t=map(int,input().split())
    s,g,h=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d=map(int,input().split())
        graph[a].append((d,b))
        graph[b].append((d,a))

    answer=[]
    g_h=dijkstra(g,h)
    h_g=dijkstra(h,g)

    for _ in range(t):
        x=int(input())
        result=dijkstra(s,x)
        if result==dijkstra(s,g)+g_h+dijkstra(h,x):
            answer.append(x)
        elif result==dijkstra(s,h)+h_g+dijkstra(g,x):
            answer.append(x)
    answer.sort()
    for i in answer:
        print(i,end=' ')