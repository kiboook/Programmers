def solution(dirs):
	answer = 0
	road = [[[True, True, True, True] for _ in range(11)] for _ in range(11)]
	move = {
		'U': [-1, 0],
		'R': [0, 1],
		'D': [1, 0],
		'L': [0, -1],
	}
	head = {
		'U': [0, 2],
		'R': [1, 3],
		'D': [2, 0],
		'L': [3, 1],
	}

	cur_i, cur_j = [5, 5]
	for val in dirs:
		visit_i, visit_j = cur_i + move[val][0], cur_j + move[val][1]
		if 0 <= visit_i <= 10 and 0 <= visit_j <= 10:
			if road[cur_i][cur_j][head[val][0]] and road[visit_i][visit_j][head[val][1]]:
				answer += 1
				road[cur_i][cur_j][head[val][0]] = False
				road[visit_i][visit_j][head[val][1]] = False

			cur_i = visit_i
			cur_j = visit_j

	return answer


if __name__ == '__main__':
	dirs = "ULLUURRRRLLDD"
	print(solution(dirs))