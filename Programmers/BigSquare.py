def solution(board):
	answer = 0

	if len(board) == 1 or len(board[0]) == 1:
		return 1

	for i in range(1, len(board)):
		for j in range(1, len(board[0])):
			left = board[i][j - 1]
			up = board[i - 1][j]
			left_up = board[i - 1][j - 1]

			if board[i][j] == 1:
				board[i][j] = min(left, up, left_up) + 1
				answer = max(answer, board[i][j])

	return answer ** 2


# board = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
board = [[0, 1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1, 0], [1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 0, 1], [0, 0, 1, 1, 1, 0, 0]]
print(solution(board))