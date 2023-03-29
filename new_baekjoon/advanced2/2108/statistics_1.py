import sys
from collections import Counter

N = int(sys.stdin.readline())

numbers = sorted([int(sys.stdin.readline()) for _ in range(N)])

print(round(sum(numbers)/N))  # 평균값

print(numbers[N//2])  # 중앙값

if N == 1:
    print(numbers[0])
else:
    many_value1, many_value2 = Counter(numbers).most_common(2)

    if many_value1[1] == many_value2[1]:  # 최빈값
        print(many_value2[0])
    else:
        print(many_value1[0])

print(numbers[-1] - numbers[0])  # 최댓값 - 최솟값
