import sys

input = sys.stdin.readline

n = int(input())

table=[[] for _ in range(n+1)]

for i in range(1,n+1):
    table[i].append(int(input()))

def dfs(num):
    if visited[num]==False:
        visited[num]=True
        for idx in table[num]:

            top_values.add(num)
            bottom_values.add(idx)

            if top_values==bottom_values:
                answer.extend(list(bottom_values))
                return

            dfs(idx)
    visited[num]=False


answer=[]

for i in range(1,n+1):
    visited=[False]*(n+1)
    top_values=set()
    bottom_values=set()
    dfs(i)

answer=list(set(answer))

print(len(answer))
answer.sort()
for i in answer:
    print(i)

"""
딕셔너리를 활용하면

import sys

n=int(sys.stdin.readline().strip())
dic={}

for i in range(n):
    dic[i+1]=int(sys.stdin.readline().strip())
print(dic)
while True:
    valueSet=set(dic.values())
    print("valeuSEt",valueSet)
    dic={key:value for key,value in dic.items() if key in valueSet}
    print("dic",dic)
    if valueSet==set(dic.values()):
        break

print(len(dic))

for key in dic.keys():
    print(key)

와 같이 가능
"""