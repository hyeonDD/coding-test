import sys
input = sys.stdin.readline

n = int(input())

dp = [[False] * n for i in range(n)]
num = list(map(int, input().split()))

for idx in range(n):
    for start in range(n):
        end = start + idx
        if end >= n:
            break

        if idx == 0:
            dp[start][end] = True
            continue

        if idx == 1:
            if num[start] == num[end]:
                dp[start][end] = True
                continue

        if num[start] == num[end] and dp[start + 1][end - 1]:
            dp[start][end] = True

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    if dp[a - 1][b - 1]:
        print(1)
    else:
        print(0)