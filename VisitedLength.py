def check(i, start, end):

	for j in range(i):
		if start[i] == start[j] and end[i] == end[j]:
			return False

		if start[i] == end[j] and end[i] == start[j]:
			return False
	else:
		return True

def solution(dirs):
	x = 0
	y = 1
	answer = 1

	start = [[0 for i in range(2)] for j in range(len(dirs))]
	end = [[0 for i in range(2)] for j in range(len(dirs))]

	if dirs[0] == 'U':
		end[0][y] += 1
	elif dirs[0] == 'D':
		end[0][y] -= 1
	elif dirs[0] == 'R':
		end[0][x] += 1
	elif dirs[0] == 'L':
		end[0][x] -= 1

	for i in range(1, len(dirs)):
		start[i] = end[i-1]

		if dirs[i] == 'U':
			end[i][x] = start[i][x]
			if -5 <= start[i][y] + 1 <= 5:
				end[i][y] = start[i][y] + 1
			else:
				end[i][y] = start[i][y]
				continue

		elif dirs[i] == 'D':
			end[i][x] = start[i][x]
			if -5 <= start[i][y] - 1 <= 5:
				end[i][y] = start[i][y] - 1
			else:
				end[i][y] = start[i][y]
				continue

		elif dirs[i] == 'R':
			end[i][y] = start[i][y]
			if -5 <= start[i][x] + 1 <= 5:
				end[i][x] = start[i][x] + 1
			else:
				end[i][x] = start[i][x]
				continue
			
		elif dirs[i] == 'L':
			end[i][y] = start[i][y]
			if -5 <= start[i][x] - 1 <= 5:
				end[i][x] = start[i][x] - 1
			else:
				end[i][x] = start[i][x]
				continue

		if check(i, start, end):
			answer += 1
	return answer


dirs = "LULLLLLLU"
print(solution(dirs))







