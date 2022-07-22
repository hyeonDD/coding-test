from collections import Counter
input()
a=Counter(list(map(int,input().split())))
input()
b=list(map(int,input().split()))
print(*map(lambda x:a[x],b))