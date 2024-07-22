#그룹 단어 체커
#String을 입력 받아 그 String이 그룹 단어(문제에 조건이 주어짐)인지 아닌지 판별하여 그룹단어인 String의 개수를 출력하는 문제이다. 

def solution(word):
    seen = set()
    last_char = ""
    for char in word:
        if char != last_char:
            if char in seen:
                return False
            seen.add(char)
            last_char = char
    return True

def groupWords(words):
    count = 0
    for word in words:
        if solution(word):
            count += 1
    return count

# 입력 받기
N = int(input().strip())
words = [input().strip() for _ in range(N)]

# 그룹 단어의 개수 출력
print(groupWords(words))
