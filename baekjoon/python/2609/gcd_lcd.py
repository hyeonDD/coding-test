import sys

a,b = map(int,sys.stdin.readline().split())

def gcd(a,b):
    while True:
         f,e = a/b, a%b
         if e == 0:
             break
         a = b
         b = e
    return b

def lcm(a,b):    
    return a*b // gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))

