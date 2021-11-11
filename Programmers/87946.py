from itertools import permutations


def solution(k, dungeons):
    answer = float('-inf')

    # 1. 방문 할 던전 순열 구하기
    for permutations_dungeons in permutations(dungeons):
        cur_tired = k
        tmp_answer = 0
        for dungeon in permutations_dungeons:
            min_tired = dungeon[0]
            use_tired = dungeon[1]
            # 2. 현재 피로도가 최소 요구 피로도 이상이라면 던전 탐험
            if min_tired <= cur_tired:
                cur_tired -= use_tired
                tmp_answer += 1
        answer = max(tmp_answer, answer)

    return answer


if __name__ == "__main__":
    k = 80
    dungeons = [[80, 20], [50, 40], [30, 10]]

    print(solution(k, dungeons))