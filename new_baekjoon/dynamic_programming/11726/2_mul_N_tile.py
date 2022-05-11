import sys

n = int(sys.stdin.readline())

test = {0:0,1:1,2:2}
def dp(m):
    if test(m) in test:
        return test[m]
    else:
        test[m] = dp(m-1) + dp(m-2)
    
    return dp(m-2) + dp(m-1)
print(dp(n)%10007)
