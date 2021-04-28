from collections import Counter


def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    low, high = 0, 0

    for my_num in lottos:
        for win_num in win_nums:
            if my_num == win_num:
                low += 1

    high = low + Counter(lottos)[0]

    return [rank[high], rank[low]]


if __name__ == "__main__":
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]

    print(solution(lottos, win_nums))