import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
A = [*map(int,input().split())]

counter = Counter(A)

result = [-1]*N
stack = [0]

for i in range(N):
    while stack and counter[A[stack[-1]]] < counter[A[i]]:
        result[stack.pop()] = A[i]
    stack.append(i)

print(' '.join(map(str,result)))
