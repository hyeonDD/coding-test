import sys

input = sys.stdin.readline

A,B,C = list(map(int,input().split()))

if C<B or C==B:
    print(-1)
else:
    print(A//(C-B)+1)

# 3 (2 1)
# 2100000000 (9 10)
# 1000 70 170

# A < Cn-Bn

# 1000 < 100n
# 2100000000 < (10-9)n
# 3 < (1-2)n