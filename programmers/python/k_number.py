array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

# cut_array = array[commands[0][0]-1:commands[0][1]]
# print(sorted(cut_array)[2])



# print(cut_array)
# print(array)




# def solution(array, commands):
#     answer = []
#     for i in range(0,3):
#         cut_array = array[commands[i][0]-1:commands[i][1]]
#         answer.append(sorted(cut_array)[commands[i][2]-1])
#         print(answer)    
#     return answer
# solution(array,commands)


# def solution(array, commands):
#     answer = []
#     for command in commands:
#         new_array = array[command[0]-1:command[1]]
#         answer.append(sorted(new_array)[command[2]-1])
    
#     return answer

# print(solution(array,commands))

# a = list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
# print(a)

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
print(solution(array,commands))