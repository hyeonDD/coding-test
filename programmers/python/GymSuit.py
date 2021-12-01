n=5
lost=[2,4]
reserve=[3]

# def solution(n, lost, reserve):
#     min_number = n-len(lost)
#     for add in reserve:
#         if (add+1 == lost[0]) or (add+1 == lost[1]):
#             min_number+=1

#     return min_number

# print(solution(n,lost,reserve))

# def solution(n, lost, reserve):
#     set_reserve=set(reserve)-set(lost)
#     set_lost = set(lost)-set(reserve)
#     print(set_lost)
#     for i in set_reserve:
#         if i-1 in set_lost:
#             set_lost.remove(i-1)
#         elif i+1 in set_lost:
#             set_lost.remove(i+1)
#     return n-len(set_lost)


def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    print(_reserve)
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
print(solution(n,lost,reserve))