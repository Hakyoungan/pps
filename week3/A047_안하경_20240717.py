#열개씩 끊어 출력하기
#입력으로 주어진 단어를 열 개씩 끊어서 한 줄에 하나씩 출력한다.
def solution(word):
    for i in range(0, len(word), 10):
        print(word[i:i+10])

word = input().strip()
solution(word)
