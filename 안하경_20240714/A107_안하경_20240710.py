#쉽게 푸는 문제
#주어진 규칙에 맞게 배열을 만들고 그 배열에서 부분합을 구하는 문제
def makeSequence(n):
    sequence = []
    for i in range(1, n + 1):
        sequence.extend([i] * i)
    return sequence

def sumSequence(A, B):
    #큰 수열을 생성
    sequence = makeSequence(1000) 
    return sum(sequence[A-1:B])

A, B = map(int, input().split())
result = sumSequence(A, B)
print(result)
