#소인수분해
#정수가 주어졌을 때 소인수분해하는 과정을 출력하는 문제
def prime_factors(N):
    if N == 1:
        return
    
    # 2로 나누기
    while N % 2 == 0:
        print(2)
        N //= 2
    
    # 3부터 시작하여 N의 제곱근까지의 홀수를 검사
    factor = 3
    while factor * factor <= N:
        while N % factor == 0:
            print(factor)
            N //= factor
        factor += 2
        
    # 남은 수가 소수인 경우
    if N > 1:
        print(N)

N = int(input())
prime_factors(N)
