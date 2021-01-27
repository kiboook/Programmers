def dijkstra(n, graph):
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if i != j:
					cost = graph[i][k] + graph[k][j]
					if graph[i][j] > cost:
						graph[i][j] = cost
				else:
					graph[i][j] = 0
	return


def solution(n, s, a, b, fares):
	s -= 1
	a -= 1
	b -= 1
	INF = float('inf')
	answer = INF

	graph = [[INF] * n for _ in range(n)]
	for val in fares:
		start, end, cost = val[0], val[1], val[2]
		graph[start - 1][end - 1] = cost
		graph[end - 1][start - 1] = cost
	dijkstra(n, graph)

	for i in range(n):
		cost = graph[s][i] + graph[i][a] + graph[i][b]
		if answer > cost:
			answer = cost

	return answer


if __name__ == '__main__':
	# _n, _s, _a, _b = 6, 4, 6, 2
	# _fares = [[4, 1, 10],
	# 		  [3, 5, 24],
	# 		  [5, 6, 2],
	# 		  [3, 1, 41],
	# 		  [5, 1, 24],
	# 		  [4, 6, 50],
	# 		  [2, 4, 66],
	# 		  [2, 3, 22],
	# 		  [1, 6, 25]]

	# _n, _s, _a, _b = 7, 3, 4, 1
	# _fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

	_n, _s, _a, _b = 6, 4, 5, 6
	_fares = [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]

	print(solution(_n, _s, _a, _b, _fares))
