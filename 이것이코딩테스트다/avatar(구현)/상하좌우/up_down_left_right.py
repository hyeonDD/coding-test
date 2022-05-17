from shutil import move
from sys import stdin

input = stdin.readline

n = int(input())
x,y = 1, 1
routes = input().strip().split()
# print(route)

dx = [0, 0, -1 , 1]
dy = [-1, 1, 0, 0]
move_types = ['L','R','U','D']

for route in routes:
    for i in range(len(move_types)):
        if route == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x,y)