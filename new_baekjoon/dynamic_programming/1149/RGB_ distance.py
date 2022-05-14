import sys

N = int(sys.stdin.readline())

cost = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# 첫번째집을 아예 배재후, 가장 작은 값을 찾기
for i in range(1,N):
    cost[i][0] = min(cost[i-1][1],cost[i-1][2]) + cost[i][0]
    cost[i][1] = min(cost[i-1][0],cost[i-1][2]) + cost[i][1]
    cost[i][2] = min(cost[i-1][0],cost[i-1][1]) + cost[i][2]

print(min(cost[N-1]))