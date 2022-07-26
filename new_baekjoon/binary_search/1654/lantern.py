k,n=map(int,input().split())
lan_lines=[int(input()) for _ in range(k)]
start,end=1,max(lan_lines)

while start<=end:
    mid = (start+end) // 2
    lines=0
    for i in lan_lines:
        lines += i//mid
    if lines >= n:
        start = mid+1
    else:
        end = mid-1
print(end)

"""
25 421
25468
42380
34638
19901
35751
24933
15368
854
24429
35451
32479
22039
24149
45061
34767
5716
13347
11121
19624
12193
34154
24840
40357
5152
42609
"""