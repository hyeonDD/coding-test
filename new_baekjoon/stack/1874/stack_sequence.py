import sys
input=sys.stdin.readline

n=int(input())

org_stack=[int(input()) for _ in range(n)]

sorted_org_stack=sorted(org_stack)

stack=[]
make_stack=[]
answer=[]
idx=0
for i in sorted_org_stack:
    stack.append(i)
    answer.append('+')
    while True:
        if not stack:
            break
        if stack[-1]==org_stack[idx]:
            make_stack.append(stack.pop())
            idx+=1
            answer.append('-')
        else:
            break

if org_stack == make_stack:    
    for ans in answer:
        print(ans)
else:
    print('NO')