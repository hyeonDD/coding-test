""" import sys
import re
# 55-50+40-00009-00009
# n = sys.stdin.readline().rstrip().split('-')




# result = 0
for i in n:
    if i == n[0]:
        result = eval(i)
    else:
        result -= eval(i)
print(result) """
a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)