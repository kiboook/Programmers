def solution(a, b):
    answer = 0

    for num1, num2 in zip(a, b):
        answer += (num1 * num2)

    return answer


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    b = [-5, 2, 6, 2]

    print(solution(a, b))