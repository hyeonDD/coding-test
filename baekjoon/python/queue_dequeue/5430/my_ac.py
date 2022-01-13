import sys
from array import array
""" 
def R() -> bool:
    arr.reverse()    
    return True

def D() -> bool:
    try:
        arr.pop(0)
    except IndexError:
        print('error')
        return False
    return True

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    
    while n:
        n -= 1
        funcs = sys.stdin.readline().strip()    
        arr_num = int(sys.stdin.readline())    
        arr_index = eval(sys.stdin.readline().strip())    
        
        arr = array('i', arr_index)        
        
        flag = None
        for func in funcs:            
            flag = eval(f'{func}()')
            if flag == False:
                break
        
        if flag:
            a = str(arr)[11:-1]    
            print(a) """
    
def R() -> bool:
    arr.reverse()    
    return True

def D() -> bool:
    try:
        arr.pop(0)
    except IndexError:
        print('error')
        return False
    return True

n = int(sys.stdin.readline())
    
while n:
    n -= 1
    funcs = sys.stdin.readline().rstrip()    
    arr_num = int(sys.stdin.readline())    
    arr_index = eval(sys.stdin.readline().rstrip())
    
    arr = array('i', arr_index)        
    
    flag = None
    for func in funcs:            
        flag = eval(f'{func}()')
        if flag == False:
            break
    
    if flag:
        """ a = str(arr)[11:-1]
        print(a) """
        print('[',end='')
        for i in arr:
            print(i,end='')
            if i != arr[-1]:
                print(',',end='')
        print(']')
        
