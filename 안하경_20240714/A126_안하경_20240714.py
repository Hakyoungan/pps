#한수
#각 자리가 등차수열을 이루는 수인 한수의 개수를 출력하는 문제
def is_han_number(num):
    if num < 100:
        return True
    digits = list(map(int, str(num)))
    return digits[0] - digits[1] == digits[1] - digits[2]

def count_han_numbers(N):
    count = 0
    for num in range(1, N + 1):
        if is_han_number(num):
            count += 1
    return count

N = int(input())
print(count_han_numbers(N))
