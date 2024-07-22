#큐 2
#정수를 저장하는 큐를 구현하고, 입력으로 주어지는 큐 관련 명령을 처리하는 문제
from collections import deque

def solution(commands):
    queue = deque()
    result = []

    for command in commands:
        if command.startswith('push'):# push X: 정수 X를 큐에 넣는 연산이다.
            _, num = command.split()
            queue.append(int(num))
        elif command == 'pop': #pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
            if queue:
                result.append(queue.popleft())
            else:
                result.append(-1)
        elif command == 'size': #size: 큐에 들어있는 정수의 개수를 출력한다.
            result.append(len(queue))
        elif command == 'empty': #empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
            result.append(1 if not queue else 0)
        elif command == 'front': #front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
            if queue:
                result.append(queue[0])
            else:
                result.append(-1)
        elif command == 'back': #back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다
            if queue:
                result.append(queue[-1])
            else:
                result.append(-1)

    return result

import collections

N = int(input().strip())
commands = [input().strip() for _ in range(N)]
results = solution(commands)

for res in results:
    print(res)
