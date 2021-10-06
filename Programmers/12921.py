import math


def solution(n):
    prime_list = [True for _ in range(n + 1)]
    prime_list[0] = prime_list[1] = False

    for num in range(2, int(math.sqrt(n)) + 1):
        product = 2
        product_num = num
        while product_num * product <= n:
            prime_list[product_num * product] = False
            product += 1

    return prime_list.count(True)


if __name__ == "__main__":
    print(solution(n=10))