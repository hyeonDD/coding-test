import sys
read = sys.stdin.readline

N = int(read())
cache = {1: 0, 2: 1}

def dp(n):
    if n in cache:
        return cache[n]

    # 핵심 코드
    cnt = 1 + min(dp(n//3) + n%3, dp(n//2) + n%2)
    cache[n] = cnt
    return cnt
    
print(dp(N))