import math
n_list=[]
while True:
    a = int(input())
    if a==0:
        break
    else:
        n_list.append(a)

def is_prime_range(x):
    x = x*2 # 범위는 입력받은수 ~ 입력받은수 *2 이기 때문에 2를 곱해줌
    array = [True] *(x+1)

    for i in range(2,int(math.sqrt(x))+1):
        if array[i] == True:
            j=2
            while i*j <= x:
                array[i*j] = False
                j+=1    
    return len(list(filter(lambda a: a>x//2 and a<=x ,[i for i in range(2,x+1) if array[i]]))) # 구하고자하는 범위는 입력받은수 ~ 입력받은수*2 이기 때문에 x//2 ~ x 까지가 범위

for n in n_list:
    print(is_prime_range(n))
