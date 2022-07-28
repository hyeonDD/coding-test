import sys
input=sys.stdin.readline
n=int(input())
array=[]
for _ in range(n):
    command=input().strip()
    if command.startswith('push'):
        array.append(int(command.split()[1]))
    elif command=='pop':
        try:
            print(array.pop())
        except IndexError:
            print(-1)
    elif command=='size':
        print(len(array))
    elif command=='empty':
        if len(array)==0:
            print(1)
        else:
            print(0)
    elif command=='top':
        if len(array)==0:
            print(-1)
        else:
            print(array[-1])

"""
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
"""