# 이진탐색을 사용하는 방법
""" import sys

input = sys.stdin.readline

def binary_search(array, target, start, end):
    if start > end:
        # return None
        return "no"
    
    mid = (start + end) // 2

    if array[mid] == target:
        return "yes"
    elif array[mid] > target: # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인 (시작점은 그대로, 끝점을 중간점의 -1로)
        return binary_search(array, target, start, mid - 1)
    else : # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인 (시작점을 중간점의+1로, 끝점은 그대로)
        return binary_search(array, target, mid+1,end)
    
n = int(input())
array = sorted(list(map(int,input().split())))

m = int(input())
array2 = list(map(int,input().split()))
print(array,array2)
for target in array2:
    print(binary_search(array,target,0,n-1),end=' ') """

# 집합 자료형을 이용하는 방법

n = int(input())

array = set(map(int,input().split()))

m = int(input())

array2 = list(map(int,input().split()))

for i in array2:
    if i in array:
        print('yes',end=' ')
    else:
        print('no',end=' ')