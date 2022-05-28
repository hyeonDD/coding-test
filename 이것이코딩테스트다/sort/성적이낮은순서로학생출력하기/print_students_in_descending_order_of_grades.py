# key를 함수로 사용하는 방식

""" n = int(input())

array = [tuple(input().split()) for _ in range(n)]

def lowScore(data):
    return data[1]

array = sorted(array,key=lowScore)

for i in array:
    print(i[0],end=' ') """

# key를 람다식으로 사용하는 방법

n = int(input())

array = [tuple(input().split()) for _ in range(n)]

array = sorted(array,key= lambda student:student[1])

for i in array:
    print(i[0], end=' ')
