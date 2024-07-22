#Maximum number of balloons
#주어진 텍스트를 활용하여 "balloon"이라는 단어를 최대한 많이 만드는 문제
from collections import Counter

def maxNum(text):
    char_count = Counter(text)
    balloon = Counter("balloon")
    instances = float('inf') 
    for char in balloon:
        instances = min(instances, char_count[char] // balloon[char])
    
    return instances

text = input("Enter the text: ")
print(maxNum(text))   
