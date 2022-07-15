import sys
x = int(sys.stdin.readline())

a,b,flag=1,1,0
while x>1:
    if flag==0:
        b+=1
        flag +=1
        x -= 1
    elif flag==1:
        for _ in range(b):
            if b==1 or x==1:
                break
            a+=1
            b-=1
            x-=1
        flag +=1        
    elif flag==2:           
        a+=1
        flag+=1
        x-=1        
    elif flag==3:
        for _ in range(a):
            if a==1 or x==1:
                break
            a-=1
            b+=1
            x-=1
        flag=0

    

print(str(a)+'/'+str(b))