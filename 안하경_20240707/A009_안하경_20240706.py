#문자열 다루기 기본
#문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수 작성

def isNum(s):
    return(len(s)==4 or len(s)==6) and s.isdigit()

s=input("문자열을 입력하세요: ")
print(isNum(s))