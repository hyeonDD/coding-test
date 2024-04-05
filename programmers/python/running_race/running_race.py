def solution(players, callings):
    to_dict = {player: num for num, player in enumerate(players)}
    answer = []

    for name in callings:
        num = to_dict[name]

        front_name = players[num-1]

        # 지명한 이름 앞으로 땡기기
        to_dict[players[num]] = num-1
        # 앞에 사람 뒤로 땡기기
        to_dict[players[num-1]] = num

        players[num-1] = name
        players[num] = front_name

    return players

# 1등은 못부름
# players 순서대로 초깃값 세팅 0,1,2,3,...,n
# callings 각이름으로 앞사람과 치환
