#나이순 정렬
#나이와 이름이 주어졌을 때, 나이 순으로 나이와 이름을 정렬하는 문제.
def solution(members):
    members.sort(key=lambda x: (x[0], x[2]))
    return members

N = int(input().strip())
members = []
for i in range(N):
    age, name = input().strip().split()
    members.append((int(age), name, i))

sorted_members = solution(members)
for age, name, _ in sorted_members:
    print(age, name)
