import sys
input=sys.stdin.readline

n=int(input())

for _ in range(n):
    string=list(input().strip())
    tmp=0
    for str in string:
        if str=='(':
            tmp+=1
        else:
            tmp-=1
        if tmp<0:
            print('NO')
            break
    if tmp==0:
        print('YES')
    elif tmp>0:
        print('NO')