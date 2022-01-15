""" 
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
"""
n = int(input())
time = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))
ans = end = 0
for s, e in time:
    if s >= end:
        ans += 1
        end = e
print(ans)

