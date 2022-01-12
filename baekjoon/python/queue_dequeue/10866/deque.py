import collections
import sys

Q = collections.deque([])
answer = []

n = int(sys.stdin.readline())
while n:
    n -= 1
    command = str(sys.stdin.readline().strip())
    # print(f'======================\n {command}======================\n')
    if command.startswith('push_front'):
        Q.appendleft(int(command.split()[1]))        
    elif command.startswith('push_back'):
        Q.append(int(command.split()[1]))        
    elif command == 'pop_front':
        try :
            print(Q.popleft())
        except IndexError:
            print(-1)
    elif command == 'pop_back':
        try :
            print(Q.pop())
        except IndexError:
            print(-1)
    elif command == 'size':
        print(len(Q))
    elif command == 'empty':
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':        
        try :
            print(Q[0])
        except IndexError:
            print(-1)
    elif command == 'back':
        try :
            print(Q[-1])            
        except IndexError:
            print(-1)            

