import sys
n,m=map(int,input().split())
trees=list(map(int,input().split()))
start,end=1,max(trees)

while start<=end:
    mid=(start+end)//2    
    len_tree=0
    for tree in trees:
        if tree>mid:
            len_tree+=tree-mid
    if len_tree==m:        
        print(mid)
        sys.exit(0)
    if len_tree>=m:
        start=mid+1
    else:
        end=mid-1
print(end)

"""
10 80
2 2 3 5 9 12 12 16 18 19
#1
"""

"""
4 10
5 5 5 12
#4
"""

"""
4 7
20 15 10 17
#15
"""

"""
5 20
4 42 40 26 46
#36
"""