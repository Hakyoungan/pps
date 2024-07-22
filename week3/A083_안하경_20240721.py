#중복 빼고 정렬하기
#N개의 정수가 주어졌을 때, 중복을 제외하고 오름차순으로 정렬하는 문제.

N = int(input().strip())
numbers = list(map(int, input().strip().split()))

# 중복 제거하고 정렬
unique_numbers = sorted(set(numbers))
print(" ".join(map(str, unique_numbers)))
