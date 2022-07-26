from bisect import bisect_left,bisect_right

input()
a_list=sorted(map(int,input().split()))
input()
b_list=list(map(int,input().split()))

def count_by_range(a,obj):
    left = bisect_left(a,obj)    
    right = bisect_right(a,obj)
    return right-left

for b in b_list:
    if count_by_range(a_list,b)>=1:
        print(1)
    else:
        print(0)