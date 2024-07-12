#나머지
#수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 문제

def solution(numbers):
    remainders = set()
    for number in numbers:
        remainders.add(number % 42)
    return len(remainders)

numbers = [int(input()) for _ in range(10)]

print(solution(numbers))
