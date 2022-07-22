import sys
input=sys.stdin.readline
input()
a=set(map(int,input().split()))
input()
b=list(map(int,input().split()))
b_set=set(b)
common=b_set&a
for i in b:
    if i in common:
        print(1,end=' ')
    else:
        print(0,end=' ')