#하샤드 수
#양의 정수 x의 각 자리수의 합으로 x가 나누어졌을 때 나머지가 0인지 아닌지 판별하는 문제이다. 
def solution(x):
    # x의 각 자리스의 합
    digit_sum = sum(int(digit) for digit in str(x))
    
    # 나누어졌을 때 나머지가 0인지
    return x % digit_sum == 0

x = int(input())

print(solution(x))
