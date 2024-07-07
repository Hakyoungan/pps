#음계 판별하기
#8개의 숫자를 입력 받고(1부터 8(음계)), 오름차 순이면 ascending, 내림차순이면 descending, 둘 다 아니면 mixed 출력

def harmony(arr):
    #두가지 경우를 체크
    ascending=list(range(1,9))
    descending=list(range(8,0,-1))

    #알맞게 출력
    if arr==ascending:
        return "ascending"
    elif arr==descending:
        return "descending"
    else:
        return "mixed"
    
#문자열로 입력받은 후 정수로 된 리스트로 만들기
print("1~8의 숫자를 원하는 순서로 입력해주세요(숫자간 띄어쓰기 필수): ")
inputa = list(map(int, input().split()))

print(harmony(inputa))
