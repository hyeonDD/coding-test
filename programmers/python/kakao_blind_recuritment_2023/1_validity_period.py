# def solution(today="2022.05.19", terms=["A 6", "B 12", "C 3"], privacies=["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]):
def solution(today="2020.01.01", terms=["Z 3", "D 5"], privacies=["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]):
    answer = []
    terms_dict={term.split()[0]:int(term.split()[1]) for term in terms}
    
    today_y,today_m,today_d = map(int,today.split('.'))

    for privacy in enumerate(privacies,1):
        num,objects = privacy
        past,__terms = objects.split()
        past_y,past_m,past_d = map(int,past.split('.'))

        total = 0

        total += (today_y-past_y) * 336 # y
        total += (today_m-past_m) * 28 # m
        total += (today_d-past_d) # d

        print(total,terms_dict[__terms]*28)
        if total >= terms_dict[__terms] * 28:
            answer.append(num)

    return answer

print(solution())