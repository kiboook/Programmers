def solution(dirs):
	answer = 0
	road = [[[0, 0, 0, 0] for _ in range(11)] for _ in range(11)]
	move = {
		'U': [-1, 0],
		'R': [0, 1],
		'D': [1, 0],
		'L': [0, -1]
	}

	cur_i, cur_j = 5, 5
	for val in dirs:
		visit_i, visit_j = cur_i + move[val][0], cur_j + move[val][1]
		if 0 <= visit_i <= 10 and 0 <= visit_j <= 10:
			if val == 'U':
				if road[cur_i][cur_j][0] == 0 and road[visit_i][visit_j][2] == 0:
					answer += 1
					road[cur_i][cur_j][0] = 1
					road[visit_i][visit_j][2] = 1
			if val == 'R':
				if road[cur_i][cur_j][1] == 0 and road[visit_i][visit_j][3] == 0:
					answer += 1
					road[cur_i][cur_j][1] = 1
					road[visit_i][visit_j][3] = 1
			if val == 'D':
				if road[cur_i][cur_j][2] == 0 and road[visit_i][visit_j][0] == 0:
					answer += 1
					road[cur_i][cur_j][2] = 1
					road[visit_i][visit_j][0] = 1
			if val == 'L':
				if road[cur_i][cur_j][3] == 0 and road[visit_i][visit_j][1] == 0:
					answer += 1
					road[cur_i][cur_j][3] = 1
					road[visit_i][visit_j][1] = 1
			cur_i = visit_i
			cur_j = visit_j

	return answer


if __name__ == '__main__':
	dirs = "ULLUURRRRLLDD"
	print(solution(dirs))