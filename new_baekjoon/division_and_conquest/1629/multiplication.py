import sys

input=sys.stdin.readline

a,b,c=map(int,input().split())

def quick_mul(x,y,c):
    if y==1:
        return x%c
    elif y==2:
        return a*a%c
    else:
        if y%2:
            return ((quick_mul(x,y//2,c)**2)*x)%c
        else:
            return ((quick_mul(x,y//2,c)**2))%c

print(quick_mul(a,b,c))