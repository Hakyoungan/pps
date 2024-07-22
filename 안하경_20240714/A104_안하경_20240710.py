#욱제는 효도쟁이야!
#원형 산책로(그래프)에서 모든 마을(노드)를 방문 하기 위한 최소이동비용을 계산
def minimum_tour_cost(n, costs):
    # 총 이동 비용 합 계산
    total_cost = sum(costs)
    
    # 최소 이동 비용을 찾기 위한 변수 초기화
    min_cost = float('inf')
    
    # 이동 비용을 누적하여 최소값을 찾는 방법
    for i in range(n):
        # i번째 마을에서 시작하는 경우의 이동 비용 계산
        cost = total_cost - costs[i]
        if cost < min_cost:
            min_cost = cost
            
    return min_cost

n = int(input())
costs = list(map(int, input().split()))

result = minimum_tour_cost(n, costs)
print(result)