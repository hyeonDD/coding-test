import collections
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    # print(answer.keys())
    return list(answer.keys())[0]

print(solution(participant,completion))