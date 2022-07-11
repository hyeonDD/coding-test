import math
def solution(fees, records):
    records = [record.split() for record in records]
    # 레코드 차량번호 순으로 정렬
    records.sort(key=lambda x : x[1])
    
    car_time = []
    answer ={}
    for record in records:
        car_time.append(record[0])
        answer[(record[1])]=0

    for i in range(len(car_time)):
        hour,minute = car_time[i].split(':')
        car_time[i] = (int(hour)*60) + int(minute)
    # 입차, 출차 기준으로 누적시간 계산
    for record in records:
        # record[1]
        index = records.index(record)
        if record[2]=='IN':
            answer[record[1]] += -(car_time[index])
        elif record[2]=="OUT":
            answer[record[1]] += car_time[index]

    # 누적시간 계산 (출차가된 없는 차의 기록 예외처리)
    for key,value in answer.items():
        if value < 0 or value==0:
            answer[key] += 1439
    answer2 = []
    
    # 기본 주차시간 미초과시 기본요금 부여 or 주차시간 초과시 추가정산 math.ceil은 올림 메서드
    for time in answer.values():
        print(time)
        if time > fees[0]:
            answer2.append(fees[1] + (math.ceil((time-fees[0])/fees[2]))*fees[3])
        else:
            answer2.append(fees[1])
    return answer2




solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
# solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]) # [0, 591]
# solution([1, 461, 1, 10],["00:00 1234 IN"]) #[14841]
