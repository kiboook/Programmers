from itertools import combinations


def solution(numbers):
    answer = set()

    for item in combinations(numbers, 2):
        answer.add(sum(item))

    return sorted(list(answer))


if __name__ == "__main__":
    numbers = [0, 0, 0]
    print(solution(numbers))