import math
cnt=0
for i in str(math.factorial(int(input())))[::-1]:
    if i!='0':
        break
    cnt+=1
print(cnt)