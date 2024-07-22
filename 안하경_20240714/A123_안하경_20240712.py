#1로 만들기
#특정한 규칙에 따라 정수를 1로 만드는 문제
def min_operations_to_one(N):

    dp = [0] * (N + 1)
    
    for i in range(2, N + 1):
        # 1을 뺀다
        dp[i] = dp[i - 1] + 1
        
        # X가 2로 나누어 떨어지면, 2로 나눈다.
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        
        # X가 3으로 나누어 떨어지면, 3으로 나눈다.
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    return dp[N]

N = int(input())
print(min_operations_to_one(N))
