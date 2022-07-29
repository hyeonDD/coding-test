import sys
input=sys.stdin.readline
n=int(input())
array=list(map(int,input().split()))

stack=[]
max_num=max(array)
answer=[-1 for i in range(n)]
for i in range(n-1):
    stack.append(i) # stack에 idx push
    if array[stack[-1]]<array[i+1]: # 스택의 마지막수가 다음수 보다 작으면
        while stack:
            if array[stack[-1]]<array[i+1]: # 스택중 작은 수들만 answer에 넣기
                answer[stack.pop()]=array[i+1]
            else:
                break
    elif array[stack[-1]]==max_num:
        answer[stack.pop()]=-1

print(*answer)