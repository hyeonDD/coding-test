import sys
input = sys.stdin.readline

chu_N = int(input())
chu_list = list(map(int,input().split()))

glass_ball_N = int(input())
ball_list = list(map(int,input().split()))

dp_chu = {i:False for i in range(sum(chu_list)+1)}
dp_chu[0] = True

for chu in chu_list:
    for sum_chu, exist in list(dp_chu.items()):
        if exist:
            if not dp_chu[sum_chu+chu]:
                dp_chu[sum_chu+chu] = True

for chu in chu_list:
    for sum_chu, exist in list(dp_chu.items()):
        if exist:
            if sum_chu-chu >=0 and not dp_chu[sum_chu-chu]:
                dp_chu[sum_chu-chu] = True

for ball in ball_list:
    if ball > sum(chu_list):
        print("N", end= " ")
        continue
    if dp_chu[ball]:
        print("Y", end=" ")
    else:
        print("N", end=" ")