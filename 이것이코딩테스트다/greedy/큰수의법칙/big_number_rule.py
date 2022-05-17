from sys import stdin

input = stdin.readline

N,M,K = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()

first = arr[-1]
second = arr[-2]

count = M//(K+1) * K
count += M % (K + 1)

result = 0

result += count * first
result += (M - count) * second

print(result)


