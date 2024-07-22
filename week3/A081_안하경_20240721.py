#N번째 큰 수
#배열 A가 주어졌을 때, N번째 큰 값을 출력하는 프로그램
def solution(array):
    # 내림차순 정렬
    sorted_array = sorted(array, reverse=True)
    # 세번째 큰 값!
    return sorted_array[2]

T = int(input().strip())
for _ in range(T):
    array = list(map(int, input().strip().split()))
    print(solution(array))
