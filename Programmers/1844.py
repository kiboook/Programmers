from collections import deque


def BFS(maps):
    row = len(maps)
    col = len(maps[0])

    visit = [[False for _ in range(col)] for _ in range(row)]
    visit[0][0] = True
    queue = deque([[0, 0, 1]])
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    while queue:
        now_i, now_j, move = queue.popleft()
        if now_i == row - 1 and now_j == col - 1:
            return move
        for value in dirs:
            visit_i, visit_j = now_i + value[0], now_j + value[1]
            if 0 <= visit_i < row and 0 <= visit_j < col and not visit[visit_i][visit_j]:
                if maps[visit_i][visit_j] == 1:
                    queue.append([visit_i, visit_j, move + 1])
                    visit[visit_i][visit_j] = True
    return -1


def solution(maps):
    answer = BFS(maps)
    return answer


if __name__ == "__main__":
    maps = [[1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1]]

    print(solution(maps))