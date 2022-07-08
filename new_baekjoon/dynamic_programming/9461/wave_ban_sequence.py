import sys

N = int(sys.stdin.readline())

test_case = [int(sys.stdin.readline()) for i in range(N)]

d = {n:-1 for n in range(102)}
d[1] = 1
d[2] = 1
d[3] = 1
def dp(num):
    if d[num] != -1:
        return d[num]
    else:
        d[num] = dp(num-3) + dp(num-2)
    d[num] = dp(num-3) + dp(num-2)
    
    return d[num]

for i in test_case:
    print(dp(i))