def solution(id_list, reports, k):
    # 신고당한 카운트수 초기화
    reported_cnt = {id:0 for id in id_list}
    # 신고한 사람 초기화
    report_person = {id:[] for id in id_list}
    
    # 중복제거
    reports = list(set(reports))
    report = []
    for _report in reports:
        report.append(_report.split())

    # 신고당한 횟수와 신고한사람과 신고한사람 명단작성
    for i in range(len(report)):
        reported_cnt[f'{report[i][1]}'] += 1
        report_person[f'{report[i][0]}'] += [f'{report[i][1]}']

    answer = [0] * len(id_list)

    for key,value in reported_cnt.items():
        # print(key,value)
        if value >= k:
            for i in range(len(id_list)):
                if key in report_person[f'{id_list[i]}']:
                    answer[i] += 1
    print(answer)
    return answer

    

# solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)
solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3)