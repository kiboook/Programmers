def solution(n, costs):
	answer = 0
	costs.sort(key=lambda x: x[2])
	connection = [0]

	while len(connection) != n:
		for i in costs:
			start, end, cost = i
			if start in connection and end in connection:
				continue

			if start in connection or end in connection:
				connection.append(start)
				connection.append(end)
				connection = list(set(connection))
				answer += cost
				break

	return answer


if __name__ == '__main__':
	n = 4
	costs = [[0, 1, 9], [0, 3, 10], [1, 3, 1], [1, 2, 2], [2, 3, 3]]
	print(solution(n, costs))