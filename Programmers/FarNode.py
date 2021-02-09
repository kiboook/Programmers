import collections


def solution(n, edge):
	answer = []
	graph = {i: [] for i in range(1, n + 1)}
	visit = {i: 0 for i in range(1, n + 1)}

	for val in edge:
		start, end = val
		graph[start].append(end)
		graph[end].append(start)

	queue = collections.deque([[1, 0]])
	visit[1] = 1

	while queue:
		cur_node, dist = queue.popleft()
		for node in graph[cur_node]:
			if visit[node] == 0:
				visit[node] = 1
				queue.append([node, dist + 1])
				answer.append(dist + 1)

	return collections.Counter(answer)[max(answer)]


if __name__ == '__main__':
	n = 6
	vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
	print(solution(n, vertex))