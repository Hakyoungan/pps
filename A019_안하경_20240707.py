#숫자의 개수
#세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 문제

def solution(a,b,c):
    result = a * b * c

    # 문자열로 바꾸기
    result_str = str(result)

    # 각 숫자의 빈도를 저장할 리스트 초기화
    digit_count = [0] * 10

    # 결과 문자열에서 각 숫자의 빈도를 계산
    for char in result_str:
        digit_count[int(char)] += 1

    # 각 숫자의 빈도를 출력
    for count in digit_count:
        print(count)

a=int(input())
b=int(input())
c=int(input())
solution(a,b,c)