from itertools import combinations_with_replacement as cwr
from collections import Counter

def solution(n, info) :
    answer = []
    info = info[::-1]
    max_n = -1
    k = len(info)
    
    for c in cwr(range(0, k), n) :
        ryan = 0
        apeach = 0
        tmp_ans = [0 for _ in range(k)]
        c = Counter(c)        
        for i in range(0, k) :
            if info[i] < c[i] : # 개수가 더 많으면 라이언이 승
                ryan += i
            elif info[i] != 0 : # 아니면 어피치가 승
                apeach += i

            tmp_ans[i] = c[i]
            # print(tmp_ans)
        if ryan > apeach :
            diff = ryan - apeach            
            if max_n < diff :                
                max_n = diff
                answer = tmp_ans
               
    if answer :
        return answer[::-1]
    else :
        return [max_n]


print(solution(5,[2,1,1,1,0,0,0,0,0,0,0])) # [0,2,2,0,1,0,0,0,0,0,0]
# solution(1,[1,0,0,0,0,0,0,0,0,0,0]) # [-1]
# solution(9,[0,0,1,2,0,1,1,1,1,1,1]) # [1,1,2,0,1,2,2,0,0,0,0]
# solution(10,[0,0,0,0,0,0,0,0,3,4,3]) # [1,1,1,1,1,1,1,1,0,0,2]