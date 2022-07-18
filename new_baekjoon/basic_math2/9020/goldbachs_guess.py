def Goldbach():
    check = [False, False] + [True] * 10000
    
    for i in range(2, 101):
        if check[i] == True:
            for j in range(i + i, 10001, i):
                check[j] = False    
    T = int(input())
    for _ in range(T):
        n = int(input())

        A = n // 2 ## 입력받은수를 2로나누어서 찾는 로직 반복횟수를 줄여줌
        B = A
        for _ in range(10000):
            if check[A] and check[B]:
                print(A, B)
                break
            A -= 1
            B += 1

Goldbach()