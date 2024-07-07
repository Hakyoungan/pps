#검증수
#고유번호 5자리의 숫자들이 빈칸을 사이에 두고 하나씩 주어지면, 각 숫자를 제곱한 수들의 합을 10으로 나눈 나머지를 구하는 문제

numbers = list(map(int, input().split()))

# 처음 5자리의 숫자를 각각 제곱한 수의 합
sum= sum(num ** 2 for num in numbers)

# 을 10으로 나눈 나머지
verification = sum % 10

# 결과 출력
print(verification)
