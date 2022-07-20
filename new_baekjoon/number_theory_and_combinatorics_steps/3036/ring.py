from fractions import Fraction
n=int(input())
rings=list(map(int,input().split()))

for i in range(1,n):
    if rings[0]%rings[i]==0:
        print(f'{rings[0]//rings[i]}/1')
    else:
        print(f'{Fraction(rings[0],rings[i])}')
