from itertools import combinations


def solution(line):
    # Ax + By + E = 0
    # Cx + Dy + F = 0
    # x = BF - ED / AD - BC
    # y = EC - AF / AD - BC
    answer = list()
    cross_point = list()

    # 1. 조합을 통해 모든 선분의 교점을 찾는다.
    for lines in combinations(line, 2):
        A, B, E = lines[0]
        C, D, F = lines[1]

        check = (A * D) - (B * C)

        if check != 0:
            x = ((B * F) - (E * D)) / check
            y = ((E * C) - (A * F)) / check

            # 2. 교점이 정수인 경우에만 리스트에 삽입한다.
            if x == int(x) and y == int(y):
                cross_point.append((int(x), int(y)))

    # 3. 가장 왼쪽 위에 있는 교점과 가장 오른쪽 아래에 있는 교점을 통해 사각형을 그린다.
    cross_point.sort()
    max_x = cross_point[-1][0]
    min_x = cross_point[0][0]
    weight = max_x - min_x

    cross_point.sort(key=lambda i: i[1])
    max_y = cross_point[-1][1]
    min_y = cross_point[0][1]
    height = max_y - min_y

    rectangle = [["." for _ in range(weight + 1)] for _ in range(height + 1)]

    # 4. 교점의 좌표를 알맞게 수정해 별을 그린다.
    for point in cross_point:
        x = point[0]
        y = point[1]
        rectangle[max_y - y][x - min_x] = '*'

    for val in rectangle:
        answer.append("".join(val))
    return answer


if __name__ == "__main__":
    line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
    print(solution(line))