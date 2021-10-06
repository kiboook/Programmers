def check_arr(arr, weight, x, y):
    pivot = arr[x][y]
    for i in range(x, x + weight):
        for j in range(y, y + weight):
            if arr[i][j] != pivot:
                return [False, -1]

    return [True, pivot]


def egg_arr(arr, weight, i, j, answer):
    result = check_arr(arr, weight, i, j)

    if result[0]:
        answer[result[1]] += 1
        return
    else:
        weight //= 2
        egg_arr(arr, weight, i, j, answer)
        egg_arr(arr, weight, i + weight, j, answer)
        egg_arr(arr, weight, i, j + weight, answer)
        egg_arr(arr, weight, i + weight, j + weight, answer)


def solution(arr):
    answer = [0, 0]
    egg_arr(arr, len(arr), 0, 0, answer)

    return answer


if __name__ == "__main__":
    arr = [[1, 1, 1, 1, 1, 1, 1, 1],
           [0, 1, 1, 1, 1, 1, 1, 1],
           [0, 0, 0, 0, 1, 1, 1, 1],
           [0, 1, 0, 0, 1, 1, 1, 1],
           [0, 0, 0, 0, 0, 0, 1, 1],
           [0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 1, 0, 0, 1],
           [0, 0, 0, 0, 1, 1, 1, 1]]

    print(solution(arr))