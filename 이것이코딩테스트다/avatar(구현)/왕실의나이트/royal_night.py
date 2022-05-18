from sys import stdin

input = stdin.readline

ten_num, one_num = map(int, input().strip().replace('a','1 ').replace('b','2 ').replace('c','3 ')\
    .replace('d','4 ').replace('e','5 ').replace('f','6 ').replace('g','7 ').replace('h','8 ').split())

cnt = 0

# 1. 수평으로 2칸 이동후 수직으로 한칸이동
if ten_num - 2 > 0: # 왼쪽으로 수평이동
    if one_num - 1 > 0: # 위로 수직이동
        cnt += 1
    if one_num + 1 < 9: # 아래로 수직이동
        cnt += 1
if ten_num + 2 < 9: # 오른쪽으로 수평이동
    if one_num - 1 > 0: # 위로 수직이동
        cnt += 1
    if one_num + 1 < 9: # 아래로 수직이동
        cnt += 1

# 2. 수직이동후 수평이동
if one_num -2 > 0: # 위로 수직이동
    if ten_num -1 > 0: # 왼쪽으로 수평이동
        cnt += 1
    if ten_num +1 < 9: # 오른쪽으로 수평이동
        cnt += 1
if one_num +2 < 9: #아래로 수직이동
    if ten_num -1 > 0: # 왼쪽으로 수평이동
        cnt += 1
    if ten_num +1 < 9: # 오른쪽으로 수평이동
        cnt += 1

print(cnt)