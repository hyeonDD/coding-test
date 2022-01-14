import sys
from collections import deque


n,m = map(int,sys.stdin.readline().split(' '))
a = list(map(int, sys.stdin.readline().split(' ')))

Q = deque([_ for _ in range(1,n+1)])

cnt = 0
for a in a:    
    before_len = Q.index(a)
    after_len = n - Q.index(a)
    if before_len<after_len:        
        cnt += before_len
        Q.rotate(-before_len)
    else:        
        cnt += after_len
        Q.rotate(after_len)
    Q.popleft()
    n -= 1    

print(cnt)





# 10 3
# 2 9 5

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 1  << 1 1
# 3, 4, 5, 6, 7, 8, 9, 10, 1
# 9, 10, 1, 3, 4, 5, 6, 7, 8 >> 3     3
# 10, 1, 3, 4, 5, 6, 7, 8 
# 5, 6, 7, 8, 10, 1, 3, 4 >> 4        4
