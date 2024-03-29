from collections import deque


def solution(n):
    if n == 1:
        return [1]

    answer = list()
    snail = [[0 for _ in range(n)] for _ in range(n)]
    visit = [[False for _ in range(n)] for _ in range(n)]
    visit[0][0] = True

    # 1. 남, 동, 북서 이동방향
    dirs = [[1, 0], [0, 1], [-1, -1]]
    queue = deque([[0, 0, 0, 1]])
    while queue:
        now_i, now_j, head, value = queue.popleft()
        snail[now_i][now_j] = value

        # 2. 이동방향으로 인덱스 이동
        visit_i = now_i + dirs[head][0]
        visit_j = now_j + dirs[head][1]
        # 3. 해당 인덱스로 이동 가능한 경우
        if 0 <= visit_i < n and 0 <= visit_j < n and not visit[visit_i][visit_j]:
            queue.append([visit_i, visit_j, head, value + 1])
        # 4. 해당 인덱스로 이동할 수 없다면 방향 수정
        else:
            visit_i = now_i + dirs[(head + 1) % 3][0]
            visit_j = now_j + dirs[(head + 1) % 3][1]
            # 5. 수정한 방향으로 이동
            if 0 <= visit_i < n and 0 <= visit_j < n and not visit[visit_i][visit_j]:
                queue.append([visit_i, visit_j, (head + 1) % 3, value + 1])
        visit[visit_i][visit_j] = True

    for i in snail:
        for num in i:
            if num != 0:
                answer.append(num)
    return answer


if __name__ == "__main__":
    n = 10
    print(solution(n))