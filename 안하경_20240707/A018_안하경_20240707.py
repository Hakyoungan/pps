#보물
#정수 배열 A와 B의 값을 곱하는 프로그램. 결과 값을 가장 작게 만들기 위해 A의 수를 재배열 하여 최솟값을 출력하는 문제
def solution(n,a,b):
    #오름차순으로 정렬
    sortedA=sorted(a)
    #그대로 두고 내림차순으로 정렬된 인덱스 리스트를 생성
    sortedB = sorted(range(n), key=lambda k: b[k], reverse=True)

    S=sum(sortedA[i]*b[sortedB[i]] for i in range(n))
    return S

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 결과 출력
print(solution(n, a, b))