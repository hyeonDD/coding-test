import sys
input=sys.stdin.readline
n=int(input())

paper=[list(map(int,input().split())) for _ in range(n)]

white,blue=0,0

def cut(x,y,n):
    global white,blue
    check=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=paper[i][j]:
                cut(x,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                return
    if check==0:
        white+=1
    else:
        blue+=1
cut(0,0,n)
print(white)
print(blue)