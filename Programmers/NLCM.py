from math import gcd


def solution(nums):
    check = 1
    for cur in nums:
        check *= cur

    for i in range(1, check):
        div_cnt = 0
        for j in nums:
            if i % j == 0:
                div_cnt += 1
        if div_cnt == len(nums):
            return i

    return check


def solution2(num):
    answer = num[0]
    for n in num:
        answer = n * answer // gcd(n, answer)

    return answer


my_nums = [6, 2, 8, 14]
print(solution(my_nums))