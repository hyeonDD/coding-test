n=int(input())
n_list=list(map(int,input().split()))
a=[]

if n==1:
    print(n_list[0]**2)
else:
    n_list.sort()
    print(n_list[0]*n_list[-1])