#제로
#주어진 규칙(0이면 직전의 수를 지운다)에 따른 정수들의 합을 구하는 문제
def addition(K, numbers):
    stack = []
    for number in numbers:
        if number == 0:
            if stack:
                stack.pop()
        else:
            stack.append(number)
    
    return sum(stack)

K = int(input())
numbers = [int(input()) for _ in range(K)]
result = addition(K, numbers)
print(result)
