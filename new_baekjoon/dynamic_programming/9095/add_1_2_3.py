import sys

n = int(sys.stdin.readline())

def dp(m):
    if m == 1:
        return 1
    elif m == 2:
        return 2
    elif m == 3:
        return 4
    
    return dp(m-1)+dp(m-2)+dp(m-3)


for _ in range(n):
    m = int(sys.stdin.readline())
    print(dp(m))

