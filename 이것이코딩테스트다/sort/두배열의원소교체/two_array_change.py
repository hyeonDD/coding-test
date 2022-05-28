n,k = map(int,input().split())

array = list(map(int,input().split()))
array2 = list(map(int,input().split()))

for i in range(k):
    a = min(array)
    b = max(array2)
    if a < b:
        array[array.index(a)], array2[array2.index(b)] = array2[array2.index(b)], array[array.index(a)]
    else:
        break
    

print(sum(array))