#부녀회장이 될거야
#주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력한다. 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
def solution(k, n):
    # 2차원 배열 초기화
    apartment = [[0] * (n + 1) for _ in range(k + 1)]
    
    # 0층 초기화
    for i in range(1, n + 1):
        apartment[0][i] = i
    
    # 각 층의 각 호에 대한 사람 수 계산
    for floor in range(1, k + 1):
        for room in range(1, n + 1):
            apartment[floor][room] = apartment[floor][room - 1] + apartment[floor - 1][room]
    
    return apartment[k][n]

T = int(input().strip())
for _ in range(T):
    k = int(input().strip())
    n = int(input().strip())
    print(solution(k, n))
