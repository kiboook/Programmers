def solution(N, road, K):
	answer = 0
	INF = float("INF")
	graph = [[INF] * N for _ in range(N)]

	for i in road:
		start, end, time = i
		if graph[start - 1][end - 1] > time:
			graph[start - 1][end - 1] = time
			graph[end - 1][start - 1] = time

	for k in range(N):
		for i in range(N):
			for j in range(N):
				if i != j:
					graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
				else:
					graph[i][j] = 0

	for i in graph[0]:
		if i <= K:
			answer += 1

	return answer


if __name__ == '__main__':
	N = 5
	road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
	K = 3

	print(solution(N, road, K))