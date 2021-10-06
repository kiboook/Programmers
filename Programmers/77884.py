import math


def solution(left, right):
    answer = 0

    # 제곱수는 약수의 개수가 홀수
    for num in range(left, right + 1):
        print(int(math.sqrt(num)), math.sqrt(num), num)
        if int(math.sqrt(num)) == math.sqrt(num):
            answer -= num
        else:
            answer += num

    return answer


if __name__ == "__main__":
    left = 13
    right = 17

    print(solution(left, right))