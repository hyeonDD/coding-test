from sys import stdin

input = stdin.readline

n, m = map(int,input().split())

arr = [ list(map(int,input().split())) for _ in range(n)]

result = []

for i in range(n):
    result.append(min(arr[i]))

print(max(result))