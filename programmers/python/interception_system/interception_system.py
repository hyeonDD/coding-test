def solution(targets):
    count = 0

    targets.sort(key=lambda x: x[1])
    # 조건을 갖고있는 변수
    condition = 0

    for target in targets:
        s, e = target
        # 중복된 좌표가 없으면 count+1 하는 조건
        if s >= condition:
            count += 1
            condition = e
            print(condition)

    return count

# 요격 미사일을 최소로
# 요격 미사일은 실수인 x 좌표에서도 발사 가능
