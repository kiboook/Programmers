from string import ascii_uppercase


def make_alpha(val):
	alpha = list(ascii_uppercase)
	value = alpha.index(val)

	if value <= 13:
		pass
	else:
		value = 26 - value

	return value


def right_move(name, idx):
	cur_idx = idx
	move_cnt = 0
	while name[cur_idx] == 'A':
		cur_idx = (cur_idx + 1) % len(name)
		move_cnt += 1

	return move_cnt


def left_move(name, idx):
	cur_idx = idx
	move_cnt = 0

	while name[cur_idx] == 'A':
		cur_idx = (cur_idx - 1)
		if cur_idx < 0:
			cur_idx = len(name) - 1
		move_cnt += 1

	return move_cnt


def solution(name):
	answer = 0
	idx = 0
	finish_check = 'A' * len(name)

	while True:
		if name[idx] != 'A':
			answer += make_alpha(name[idx])
			name = name.replace(name[idx], 'A', 1)

		if name == finish_check:
			break

		right_move_cnt = right_move(name, idx)
		left_move_cnt = left_move(name, idx)

		if right_move_cnt <= left_move_cnt:
			answer += right_move_cnt
			idx += right_move_cnt

		else:
			answer += left_move_cnt
			idx -= left_move_cnt
			if idx < 0:
				idx = len(name) - left_move_cnt

	return answer


name = 'BBABAAB'
# name = 'JAN'
print(solution(name))
