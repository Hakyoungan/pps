#요세푸스 문제 0
#N명이 원을 그리며 앉아있고 양의 정수 K가 주어졌을 때, 순서대로 K번째 사람을 제거한다. 이 때, 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라 한다. N, K가 주어지면 요세푸스 순열을 구하는 문제.
def solution(n, k):
    queue = list(range(1, n + 1))
    result = []
    index = 0
    
    while queue:
        index = (index + k - 1) % len(queue)
        result.append(queue.pop(index))
    
    return result

n, k = map(int, input().strip().split())
result = solution(n, k)
print("<" + ", ".join(map(str, result)) + ">")
