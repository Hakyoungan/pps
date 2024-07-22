#소트인사이드
#주어진 수의 각 자리수를 내림차순으로 정렬하는 문제.

N = input().strip()
sorted_digits = sorted(N, reverse=True)
result = ''.join(sorted_digits)

print(result)
