from collections import Counter

for _ in range(int(input())):
    types=[]
    for _ in range(int(input())):
        name,type=input().split()
        types.append(type)
    cnt=Counter(types)
    num=1
    for value in cnt.values():
        num*=value +1
    print(num-1)
    