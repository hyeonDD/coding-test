# from sys import stdin

# input = stdin.readline

# n,k = map(int,input().split())
# cnt = 0

# while True:
#     if n == 1:
#         break
#     elif n%k == 0:
#         n /= k
#         cnt += 1
#     else:
#         n -= 1
#         cnt += 1
    
# print(cnt)

from sys import stdin

input = stdin.readline

n,k = map(int,input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    print(result)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)
