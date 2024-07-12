#평균은 넘겠지
#테스트 케이스(점수) 입력받고 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 셋째 자리까지 출력한다.

C = int(input())

# C만큼
for _ in range(C):
    # 수와 점수 입력받기
    data = list(map(int, input().split()))
    N = data[0]
    scores = data[1:]
    
    # 평균
    average = sum(scores) / N
    
    # 평균을 넘는 학생 비율
    aboveAverage = sum(1 for score in scores if score > average)
    
    # 비율계산
    ratio = (aboveAverage / N) * 100
    
    # 소수점 셋째자리까지 출력
    print(f"{ratio:.3f}%")
