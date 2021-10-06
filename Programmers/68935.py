def make_ternary(num):
    output = []
    while num:
        output.append(str(int(num % 3)))
        num //= 3

    return reversed(output)


def make_decimal(num):
    output = 0
    for index, x in enumerate(num):
        output += (3 ** index) * int(x)

    return output


def solution(n):
    answer = make_decimal("".join(make_ternary(n)))

    return answer


if __name__ == "__main__":
    n = 45

    print(solution(n))