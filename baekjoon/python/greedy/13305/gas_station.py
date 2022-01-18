"""
4
2 3 1 2
4 8 9 3 1

4*(2+3+1) + 3*(2)
24+6 = 30



4
2 3 1 2
8 4 9 3 1

8*2 + 4*(3+1) + 3*(2)
16+16+6 =38 

"""
import sys
n = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().split()))
money = list(map(int, sys.stdin.readline().split()))

res = 0
m = money[0]

for i in range(n-1):
    if money[i] < m:
        m = money[i]
    res += m * length[i]

print(res)



