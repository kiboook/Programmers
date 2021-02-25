from collections import deque


def is_another_one(pivot, check):
	diff_cnt = 0

	# 단어를 비교해 다른 부분 갯수 검색
	for a, b in zip(pivot, check):
		if a != b:
			diff_cnt += 1

	if diff_cnt != 1:
		return False
	else:
		return True


def solution(begin, target, words):
	# 변환할 수 없는 경우
	if target not in words:
		return 0

	queue = deque([])
	# 큐 초기화
	for word in words:
		if is_another_one(begin, word):
			queue.append([word, 1])

	# BFS
	while queue:
		word, work = queue.popleft()
		if word == target:
			return work
		for check in words:
			if is_another_one(word, check):
				queue.append([check, work + 1])


if __name__ == '__main__':
	begin, target = "hit", "cog"
	words = ["hot", "dot", "dog", "lot", "log", "cog"]

	print(solution(begin, target, words))