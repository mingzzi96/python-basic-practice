# 평균을 구하는 함수를 만들어 보겠습니다

# 파이썬으로 평균 구하는 함수
def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

numbers = [1, 2, 3, 4, 5]
print(average(numbers)) # 3.0

# 이런식으로 다른 사람들이 만들어 둔 코드를 가져와서 쓰기만 하면 됩니다.

# 인자값을 다 더해주는 함수
def sum(a, b, c):
    return a + b + c

result = sum(1, 2, 3)
print(result) # 6