import math

def change_to_num(n,q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

def is_prime(x):
        if x == 1:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

def solution(n, q):
    q_num = change_to_num(n,q)
    
    q_num_list = q_num.split('0')
    # print(q_num)
    # print(q_num_list)
    answer = {0:0}
    for num in q_num_list:
        if num == '':
            pass
        else:
            result = is_prime(int(num))
            if result == True:
                answer[0] += 1
    
    return answer[0]

print(solution(524287,2))
# print(solution(1000000, 30))
