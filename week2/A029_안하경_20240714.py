#문문문
#문을 규칙에 맞는 방법으로 열어야하도록 시스템을 구성하였다.  문의 개수를 입력받고 문을 여는 방법을 한줄에 하나씩 출력한다.
def open_doors(N, first_method):
    if N > 6:
        print("Love is open door")
        return
    
    methods = []
    current_method = first_method
    next_method = 1 - current_method
    
    for i in range(2, N + 1):
        methods.append(next_method)
        current_method, next_method = next_method, current_method
    
    for method in methods:
        print(method)

N = int(input().strip())
first_method = int(input().strip())
open_doors(N, first_method)

