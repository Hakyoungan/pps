#스택
#정수를 저장하는 스택을 구현하고, 입력으로 주어지는 스택 관련 명령을 처리하는 문제
def solution(commands):
    stack = []
    result = []

    for command in commands:
        #push X: 정수 X를 스택에 넣는 연산이다.
        if command.startswith('push'):
            _, num = command.split()
            stack.append(int(num))
        #pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        elif command == 'pop':
            if stack:
                result.append(stack.pop())
            else:
                result.append(-1)
        #size: 스택에 들어있는 정수의 개수를 출력한다.
        elif command == 'size':
            result.append(len(stack))
        #empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
        elif command == 'empty':
            result.append(1 if not stack else 0)
        #top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        elif command == 'top':
            if stack:
                result.append(stack[-1])
            else:
                result.append(-1)

    return result

# 입력 받기
N = int(input().strip())
commands = [input().strip() for _ in range(N)]
results = solution(commands)

# 결과 출력
for res in results:
    print(res)
