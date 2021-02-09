from collections import deque


def BFS(start, graph, visit):
	queue = deque([start])
	visit[start] = 1

	while queue:
		cur_node = queue.popleft()
		for visit_node in graph[cur_node]:
			if visit[visit_node] == 0:
				visit[visit_node] = 1
				queue.append(visit_node)
	return


def solution(n, computers):
	answer = 0
	graph = {i: [] for i in range(n)}
	for i in range(n):
		for j in range(n):
			if i != j and computers[i][j] == 1:
				graph[i].append(j)

	visit = {i: 0 for i in range(n)}
	for node in range(n):
		if visit[node] == 0:
			BFS(node, graph, visit)
			answer += 1

	return answer


if __name__ == '__main__':
	n = 3
	computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
	print(solution(n, computers))