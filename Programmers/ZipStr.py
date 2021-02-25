from collections import deque


def solution(s):
	answer = [len(s)]

	# 문자열 길이 / 2 까지 문자열 분할하기
	for i in range(1, len(s) // 2 + 1):
		split_list = deque([])

		# 단위 별로 문자열 자르기
		for j in range(0, len(s), i):
			split_list.append(s[j:j + i])
		cnt = 1
		egg = ""

		# 자른 문자열 압축하기
		pivot = split_list.popleft()
		while split_list:
			check = split_list.popleft()
			if pivot == check:
				cnt += 1
			else:
				if cnt == 1:
					egg += pivot
				else:
					egg += str(cnt) + pivot
				cnt = 1
				pivot = check

		if cnt == 1:
			egg += pivot
		else:
			egg += str(cnt) + pivot
		answer.append(len(egg))

	return min(answer)


if __name__ == '__main__':
	s = input()
	print(solution(s))