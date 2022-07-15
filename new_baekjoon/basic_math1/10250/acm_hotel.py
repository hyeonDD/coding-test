t = int(input())

def calc(h,w,n):
    YY,XX = '',''
    if n%h==0:
        YY=str((n%h)+h)
        XX=str(n//h).rjust(2,'0')
    else:
        YY=str(n%h)
        XX=str(n//h+1).rjust(2,'0')
    return YY+XX

for _ in range(t):
    h,w,n=map(int,input().split())
    print(calc(h,w,n))
