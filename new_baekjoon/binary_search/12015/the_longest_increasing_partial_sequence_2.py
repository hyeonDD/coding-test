from bisect import bisect_left
n=int(input())
array=list(map(int,input().split()))
answer=[]
for i in array:
    tmp = bisect_left(answer,i)    
    if len(answer)<=tmp:
        answer.append(i)
    else:
        answer[tmp]=i
print(len(answer))




"""
5
1 4 2 3 5
#4 (1,2,3,5)
"""

"""
6
1 2 8 2 4 8
# 4 (1,2,4,8)
"""

"""
10
1 100 2 3 4 5 6 7 8 9
#9
"""