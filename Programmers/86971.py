from collections import deque


def BFS(graph, visit, start):
    node_cnt = 1
    queue = deque([start])
    visit[start] = True

    while queue:
        node = queue.popleft()
        for visit_node in graph[node]:
            if not visit[visit_node]:
                queue.append(visit_node)
                visit[visit_node] = True
                node_cnt += 1

    return node_cnt


def solution(n, wires):
    answer = float('inf')

    # 0. 그래프 생성
    graph = {node: [] for node in range(1, n + 1)}
    for wire in wires:
        start, end = wire
        graph[start].append(end)
        graph[end].append(start)

    # 1. 단순히 엣지를 하나씩 지워보며 노드 개수를 비교한다
    for wire in wires:
        start, end = wire
        graph[start].remove(end)
        graph[end].remove(start)

        # 2. 엣지를 지운 후 트리 두 개의 노드 개수 비교하기
        visit = [False for _ in range(n + 1)]
        node_cnt = []
        for node in range(1, n + 1):
            if not visit[node]:
                node_cnt.append(BFS(graph, visit, node))
        diff_node = abs(node_cnt[0] - node_cnt[1])
        if diff_node < answer:
            answer = diff_node

        # 3. 지운 엣지 다시 추가하기
        graph[start].append(end)
        graph[end].append(start)

    return answer


if __name__ == "__main__":
    n = 9
    wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]

    print(solution(n, wires))
