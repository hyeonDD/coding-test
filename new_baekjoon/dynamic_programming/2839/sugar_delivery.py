import sys

n = int(sys.stdin.readline()) # 설탕 키로수를 입력받음
cnt = 0 # 총 설탕봉지 갯수

while (n>0): # 설탕키로수가 0kg이상일때 참
    if n%5 == 0: # 키로수가 5의배수이면 
       cnt += n//5 # 남은 키로수의 5를나눈 몫만큼 봉지갯수 추가
       print(cnt)
       break # 5의 배수이면 최대이므로 반복종료
    n -= 3 # 5의 배수가 아니면 3키로를 뺌
    cnt += 1 # 3키로 봉지개수 1개 업
    if n == 0: # 남은 키로수가 정확히 0키로이면
        print(cnt) # 3키로봉지로만 구성되어있는것이므로 참
        break
else :
    print(-1)