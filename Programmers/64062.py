from copy import deepcopy


def solution(stones, k):
    # 1. 최소 0명, 최대 징검다리의 최댓값의 사람 만큼 다리를 건널 수 있다
    left = 0
    right = max(stones)

    while left <= right:
        mid = (left + right) // 2
        tmp_stones = deepcopy(stones)

        # 2. mid 명의 사람이 다리를 건넜을 때를 계산한다
        for idx, stone in enumerate(tmp_stones):
            if stone - mid < 0:
                tmp_stones[idx] = 0
            else:
                tmp_stones[idx] = stone - mid

        # 3. 0이 연속되는 길이를 구한다
        zero_range = 0
        tmp_range = 0
        for stone in tmp_stones:
            if stone == 0:
                tmp_range += 1
            else:
                tmp_range = 0
            zero_range = max(zero_range, tmp_range)

        # 4. 0이 연속되는 가장 긴 길이는 두 가지 경우로 나눌 수 있다
        # 4-1. k 이상인 경우 건널 수 있는 사람의 수를 줄여본다
        if zero_range >= k:
            right = mid - 1
        # 4-2. k 미만인 경우 건널 수 있는 사람의 수를 늘려본다
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3

    print(solution(stones, k))