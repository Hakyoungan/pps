#카이사르 암호
#입력받은 카이사르 단어를 원래 단어로 고쳐서 출력한다.
def solution(cipher):
    text = ""
    for char in cipher:
        # ASCII 값을 3만큼 감소
        new_char = chr((ord(char) - 3 - 65) % 26 + 65)
        text += new_char
    return text

# 입력 받기
cipher = input().strip()

# 복호화 및 출력
print(solution(cipher))
