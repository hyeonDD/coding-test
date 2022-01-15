"""
5
3 1 4 3 2
"""
import sys

n = int(sys.stdin.readline())
p = sorted(list(map(int,sys.stdin.readline().split())))

result = 0

for i in range(n):
    result += p[i] * (n -i)
print(result)