import random

numbers=[] ##리스트

for num in range(0,10):
    numbers.append(random.randrange(0,10))

print("생성된 리스트 : ", numbers)

for num in range(0,10):
    if num not in numbers:
        print("생성된 데이터가 없습니다.")