import sys
input=sys.stdin.readline

n=int(input())

paper=[list(map(int,input().split())) for _ in range(n)]

answer1,answer2,answer3=0,0,0

def cut(x,y,n):
    global answer1,answer2,answer3
    num=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if num!=paper[i][j]:
                tmp=int(n//3)
                cut(x,y,tmp) #1
                cut(x,y+tmp,tmp) #2
                cut(x,y+tmp*2,tmp) #3
                cut(x+tmp,y,tmp)#4
                cut(x+tmp,y+tmp,tmp)#5
                cut(x+tmp,y+tmp*2,tmp)#6
                cut(x+tmp*2,y,tmp)
                cut(x+tmp*2,y+tmp,tmp)
                cut(x+tmp*2,y+tmp*2,tmp)                
                return
    if num==-1:
        answer1+=1
    elif num==0:
        answer2+=1
    elif num==1:
        answer3+=1

cut(0,0,n)

print(answer1)
print(answer2)
print(answer3)



