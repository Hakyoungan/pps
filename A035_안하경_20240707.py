#황성 수학
#문제에 화성 수학식에 대한 설명이 주어진다. 
# 화성 수학식이 입력으로 주어지면 그 계산 값을 출력하는 문제
#@는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자
#첫째 줄에 테스트 케이스의 개수 T가 주어진다

def mars(expression):
    parts = expression.split()
    result = float(parts[0])
    
    for operator in parts[1:]:
        if operator == '@':
            result *= 3
        elif operator == '%':
            result += 5
        elif operator == '#':
            result -= 7
    
    return result

T = int(input())#테스트 케이스의 개수
expressions = [input().strip() for _ in range(T)]

for expression in expressions:
    result = mars(expression)
    print(f"{result:.2f}")
