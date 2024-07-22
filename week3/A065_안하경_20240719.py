#좌표 정렬하기
#N개의 좌표가 주어졌을 때, 좌표들을 x좌표가 증가하는 순으로 정렬하는 문제. 이 때, x좌표가 같으면 y좌표가 증가하는 순서로 정렬.
def solution(points):
    # 점들을 정렬
    points.sort(key=lambda point: (point[0], point[1]))
    return points


N = int(input().strip())
points = []

for _ in range(N):
    x, y = map(int, input().strip().split())
    points.append((x, y))

sorted = solution(points)
for point in sorted:
    print(point[0], point[1])
