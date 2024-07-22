#비밀번호 발음하기
#문자열을 입력 받고 주어진 조건에 맞는 비밀번호인지 아닌지를 판별하는 문제
def solution(password):
    vowels = "aeiou"
    
    # 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
    if not any(char in vowels for char in password):
        return False
    
    # 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    vowel_count = 0
    consonant_count = 0
    for char in password:
        if char in vowels:
            vowel_count += 1
            consonant_count = 0
        else:
            consonant_count += 1
            vowel_count = 0
        if vowel_count == 3 or consonant_count == 3:
            return False
    
    # 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다
    for i in range(1, len(password)):
        if password[i] == password[i-1] and password[i] not in "eo":
            return False
    
    return True

while True:
    password = input().strip()
    if password == "end":
        break
    if solution(password):
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")
