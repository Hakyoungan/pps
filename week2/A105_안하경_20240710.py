#분수 찾기
#주어진 규칙에 맞게 배열에 분수를 저장하고, 규칙에 맞게 배열을 탐색
def findFraction(X):
    #n=대각선의 번호, X=대각선 내에서의 위치
    n = 1
    while X > n:
        X -= n
        n += 1
    
    if n % 2 == 0:
        # 짝수 대각선 (왼쪽 아래에서 오른쪽 위)
        numerator = X
        denominator = n - X + 1
    else:
        # 홀수 대각선 (오른쪽 위에서 왼쪽 아래)
        numerator = n - X + 1
        denominator = X
    
    return f"{numerator}/{denominator}"

X = int(input())
print(findFraction(X))
