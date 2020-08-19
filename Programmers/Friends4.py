from collections import deque


def solution(m, n, board):
	answer = 0
	board = [[val for val in low] for low in board]

	while True:
		for i in range(1, m):  # 가로로 검사해 지울 곳을 찾는 반복문
			for j in range(1, n):
				if board[i - 1][j - 1].upper() == board[i][j].upper() and board[i - 1][j].upper() == board[i][j].upper() \
						and board[i][j - 1].upper() == board[i][j].upper():

					board[i - 1][j - 1] = board[i - 1][j - 1].lower()
					board[i - 1][j] = board[i - 1][j].lower()
					board[i][j - 1] = board[i][j - 1].lower()
					board[i][j] = board[i][j].lower()

		break_point = answer
		for i in range(n):  # 세로로 검사해 내려갈 칸 수를 찾는 반복문
			low_cnt = 0
			lower_box = deque()
			upper_box = deque()
			for j in range(m):
				if board[j][i].islower():
					board[j][i] = '-'
					low_cnt += 1

			for j in range(m):
				if board[j][i] == '-':
					lower_box.append(board[j][i])
				else:
					upper_box.append(board[j][i])

			idx = 0
			while lower_box:
				board[idx][i] = lower_box.popleft()
				idx += 1

			while upper_box:
				board[idx][i] = upper_box.popleft()
				idx += 1

			answer += low_cnt

		if break_point == answer:
			break

	return answer


# n = 5
# m = 4
# board = ['AAAAA', 'AUUUA', 'AUUAA', 'AAAAA']

n = 2
m = 8
board = ['FF', 'AA', 'CC', 'AA', 'AA', 'CC', 'DD', 'FF']

# n = 2
# m = 11
# board = ['FF', 'FF', "TA", 'AB', 'BC', 'FF', 'FF', 'BC', 'CB', 'FF', 'FF']
print(solution(m, n, board))