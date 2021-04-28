from collections import deque


def solution(rows, columns, queries):
    answer = []

    # 1. 배열 초기화
    arr = [[0 for _ in range(columns)] for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num
            num += 1

    # 2. 쿼리문 마다 회전 범위 시계방향으로 구하기
    for querie in queries:
        rotate = deque([])
        rotate_index = []
        min_i, max_i = querie[0] - 1, querie[2] - 1
        min_j, max_j = querie[1] - 1, querie[3] - 1

        # 2-1 오른쪽 방향
        for j in range(min_j, max_j + 1):
            rotate.append(arr[min_i][j])
            rotate_index.append([min_i, j])

        # 2-2 아래쪽 방향
        for i in range(min_i + 1, max_i + 1):
            rotate.append(arr[i][max_j])
            rotate_index.append([i, max_j])

        # 2-3 왼쪽 방향
        for j in range(max_j - 1, min_j - 1, -1):
            rotate.append(arr[max_i][j])
            rotate_index.append([max_i, j])

        # 2-4 위쪽 방향
        for i in range(max_i - 1, min_i - 1, -1):
            rotate.append(arr[i][min_j])
            rotate_index.append([i, min_j])
        answer.append(min(rotate))

        # 2-6 회전 범위를 통해 회전 시키기
        rotate.appendleft(rotate.pop())
        for index, num in zip(rotate_index, rotate):
            arr[index[0]][index[1]] = num

    return answer


if __name__ == "__main__":
    rows = 3
    columns = 3
    queries = [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]

    print(solution(rows, columns, queries))
