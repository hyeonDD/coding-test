""" 
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
"""
import sys


n,k = map(int,sys.stdin.readline().split(' '))
std_list = reversed([int(sys.stdin.readline().rstrip()) for _ in range(n)])
cnt = 0
for i in std_list:
    while True:
        if k // i == 0:
            break
        else:
            cnt = cnt + k//i
            k %= i
print(cnt)






