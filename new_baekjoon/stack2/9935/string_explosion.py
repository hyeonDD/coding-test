import sys

input = sys.stdin.readline

input1,input2 = input().rstrip(),input().rstrip()

stack = []
len_input2 = len(input2)

for i in input1:
    stack.append(i)
    if ''.join(stack[-len_input2:]) == input2:
        for _ in range(len_input2):
            stack.pop()

print(''.join(stack) if stack else 'FRULA')