#카드2
#N장의 카드에는 차례로 1부터 N까지의 번호가 있다. N이 주어졌을 때, 제일 위에 있는 카드를 바닥에 버린 후, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기는 동작을 반복한다. 이 동작을 반복했을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램이다.
from collections import deque

def solution(n):
    queue = deque(range(1, n + 1))
    while len(queue) > 1:
        queue.popleft()  # 제일 위에 있는 카드 버리기
        queue.append(queue.popleft())  # 제일 위에 있는 카드를 제일 아래로 옮기기
    
    return queue[0]

n = int(input().strip())
print(solution(n))
