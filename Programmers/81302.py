from collections import deque


def BFS(place, start):
    visit = [[False for _ in range(5)] for _ in range(5)]
    visit[start[0]][start[1]] = True
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    start_info = start
    start_info.append(0)
    start_info.append('O')
    queue = deque([start_info])

    while queue:
        # 5. 현재 위치, 거리, 위치 정보를 가져온다.
        now_i, now_j, dist, point = queue.popleft()
        # 6. 현재 위치가 응시자이며 거리가 2 이하라면 거리두기를 하지 않은 것이다.
        if point == 'P' and dist <= 2:
            return False

        for value in dirs:
            visit_i, visit_j = now_i + value[0], now_j + value[1]
            if 0 <= visit_i < 5 and 0 <= visit_j < 5 and not visit[visit_i][visit_j]:
                if place[visit_i][visit_j] != 'X':
                    queue.append([visit_i, visit_j, dist + 1, place[visit_i][visit_j]])
                visit[visit_i][visit_j] = True

    return True


def chk_distance(place):
    people_loc = []
    # 1. 응시자들의 위치를 저장한다.
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                people_loc.append([i, j])

    for loc in people_loc:
        # 2. 응시자 별로 다른 응시자끼리와의 거리를 구한다.
        # 3. 거리두기를 하지 않고 있는 경우 탐색을 종료하고 0을 반환한다.
        if not BFS(place, loc):
            return 0

    # 4. 거리두기를 하고 있는 경우 1을 반환한다.
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(chk_distance(place))

    return answer


if __name__ == "__main__":
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
              ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
              ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
              ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
              ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

    print(solution(places))