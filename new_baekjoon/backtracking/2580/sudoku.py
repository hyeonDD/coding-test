""# from pprint import pprint
org_board=[list(map(int,input().split())) for _ in range(9)]

# print(org_board[0])
# 입력받은 보드 기준으로 0이 1개 있는 보드의 수를 채워주기
for board in org_board:
    temp=[0,1,2,3,4,5,6,7,8,9]
    if board.count(0)==1:
        for x in board:
            temp.remove(x)
        org_board[org_board.index(board)][board.index(0)]=temp[0]
# pprint(org_board)

reverse_board=list(map(list,zip(*org_board)))
# pprint(org_board)
# pprint(reverse_board)

# 입력받은것을 행,렬 반전하여 똑같은 방식으로 채우기
for board in reverse_board:
    temp=[0,1,2,3,4,5,6,7,8,9]
    if board.count(0)==1:
        for x in board:
            temp.remove(x)
        org_board[board.index(0)][reverse_board.index(board)]=temp[0]
        reverse_board[reverse_board.index(board)][board.index(0)]=temp[0]
# pprint(org_board)
# pprint(reverse_board)
print('-'*10)
for i in org_board:
    print(*i)

# pprint(reverse_board[:3])
# pprint(reverse_board[3:6])
# pprint(reverse_board[6:])

# 3*3 수도쿠 보드만들기

board33=[[],[],[],[],[],[],[],[],[]]

idx=0
for board in org_board[:3]:
    board33[idx]+=board[:3]
    board33[idx+1]+=board[3:6]
    board33[idx+2]+=board[6:]

idx=3
for board in org_board[3:6]:
    board33[idx]+=board[:3]
    board33[idx+1]+=board[3:6]
    board33[idx+2]+=board[6:]

idx=6
for board in org_board[6:]:
    board33[idx]+=board[:3]
    board33[idx+1]+=board[3:6]
    board33[idx+2]+=board[6:]

# 3*3 보드도 기존과 동일하게 0이 한개인 행만 찾아 채움
# pprint(org_board)
# pprint(board33)
for board in board33:
    temp=[0,1,2,3,4,5,6,7,8,9]
    if board.count(0)==1:
        for x in board:
            temp.remove(x)
        board33[board33.index(board)][board.index(0)]=temp[0]
# pprint(board33)

# 보드 원상복귀
answer=[[],[],[],[],[],[],[],[],[]]

idx=0
for board in board33[:3]:
    answer[idx]+=board[:3]
    answer[idx+1]+=board[3:6]
    answer[idx+2]+=board[6:]

idx=3
for board in board33[3:6]:
    answer[idx]+=board[:3]
    answer[idx+1]+=board[3:6]
    answer[idx+2]+=board[6:]

idx=6
for board in board33[6:]:
    answer[idx]+=board[:3]
    answer[idx+1]+=board[3:6]
    answer[idx+2]+=board[6:]
print('-'*10)
for i in answer:
    print(*i)
""

sudoku = [list(map(int, input().split())) for _ in range(9)]
#해결해야될 칸만 받음
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def is_promising(i, j):
    promising = [1,2,3,4,5,6,7,8,9]  
    
    #행열 검사
    for k in range(9):
        if sudoku[i][k] in promising:
            promising.remove(sudoku[i][k])
        if sudoku[k][j] in promising:
            promising.remove(sudoku[k][j])
            
    #3*3 박스 검사
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in promising:
                promising.remove(sudoku[p][q])
    
    return promising

flag = False #답이 출력되었는가?
def dfs(x):
    global flag
    
    if flag: #이미 답이 출력된 경우
        return
        
    if x == len(zeros): #마지막 0까지 다 채웠을 경우
        for row in sudoku:
            print(*row)
        flag = True #답 출력
        return
        
    else:    
        (i, j) = zeros[x]
        promising = is_promising(i, j) #유망한 숫자들을 받음
        
        for num in promising:
            sudoku[i][j] = num #유망한 숫자 중 하나를 넣어줌
            dfs(x + 1) #다음 0으로 넘어감
            sudoku[i][j] = 0 #초기화 (정답이 없을 경우를 대비)
dfs(0)