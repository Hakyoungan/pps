#베스트셀러
#제일 많이 입력받은 책의 제목을 출력하는 문제
from collections import Counter #책 제목의 빈도를 계산하기 위해

def most_sold_book(n, book_titles):
    counter = Counter(book_titles)
    most_common_count = max(counter.values())
    
    # 가장 많이 입력받은 책을 찾고 정렬하기
    most_common_books = [title for title, count in counter.items() if count == most_common_count]
    most_common_books.sort()
    
    return most_common_books[0]


N = int(input().strip())
book_titles = [input().strip() for _ in range(N)]
print(most_sold_book(N, book_titles))
