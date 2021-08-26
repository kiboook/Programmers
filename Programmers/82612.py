def solution(price, money, count):
    answer = (count * (price + price * count)) // 2 - money

    return answer if answer > 0 else 0


if __name__ == "__main__":
    price = 3
    money = 100
    count = 4

    print(solution(price, money, count))