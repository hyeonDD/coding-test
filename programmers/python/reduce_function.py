from functools import reduce

print(reduce(lambda x, y: y + x, 'abcde'))

a = 'abcde'
x = a[4]

value = next(iter(a))


# print(type(value))
print(f'a의 값은 {value} 입니다')
# print(x)
for i in range(len(a)-1):
    x = x + a[i+1]
    print(x)
# print(x)