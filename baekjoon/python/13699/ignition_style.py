import sys

# num = int(sys.stdin.readline())
"""
t(0)=1
t(n)=t(0)*t(n-1)
    +t(1)*t(n-2)
    +...+
    t(n-1)*t(0)
t(1)=t(0)*t(0)=1
t(2)=t(0)*t(1)+t(1)*t(0)=2
t(3)=
    t(0)*t(2)+
    t(1)*t(1)+t(2)*t(0)=5 """

def ignition(num):
    result = 0
    if num == 1:
        return t[0]
    elif num == 2:
        return t[1]
    elif num == 3:
        return t[2]
    elif num == 4:
        return t[3]
    for i in range(num):        
        pass


    if t[num-1]:
        pass
    else:
        for i in range(num):
            result = result + t[i] * t[i-1]

    

t = [0]*35
t[0] = 1
t[1] = 1
t[2] = 2
t[3] = 5


