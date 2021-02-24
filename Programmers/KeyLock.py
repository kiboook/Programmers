def is_unlock(lock_map, lock_len):
	for i in range(lock_len):
		for j in range(lock_len):
			if lock_map[i + lock_len][j + lock_len] == 0 or lock_map[i + lock_len][j + lock_len] == 2:
				return False

	return True


def push_key(start, lock_map, key):
	for i in range(len(key)):
		for j in range(len(key)):
			lock_map[start[0] + i][start[1] + j] += key[i][j]
	return


def pop_key(start, lock_map, key):
	for i in range(len(key)):
		for j in range(len(key)):
			lock_map[start[0] + i][start[1] + j] -= key[i][j]
	return


def solution(key, lock):
	lock_len = len(lock)
	lock_map = [[0 for _ in range(lock_len * 3)] for _ in range(lock_len * 3)]

	# 자물쇠 확장
	for i in range(lock_len):
		for j in range(lock_len):
			lock_map[i + lock_len][j + lock_len] = lock[i][j]

	for _ in range(4):
		# 90도 시계방향 회전
		for idx, spin in enumerate(zip(*key)):
			key[idx] = list(reversed(spin))

		for i in range(len(lock_map) - lock_len + 1):
			for j in range(len(lock_map) - lock_len + 1):
				push_key([i, j], lock_map, key)
				if is_unlock(lock_map, lock_len):
					return True
				pop_key([i, j], lock_map, key)

	return False


if __name__ == '__main__':
	key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
	lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
	print(solution(key, lock))