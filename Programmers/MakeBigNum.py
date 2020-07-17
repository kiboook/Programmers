from collections import deque


def solution(num, k):
	garbage_num = 0
	check_len = len(num) - k
	num = deque(num)
	answer = list()

	answer.append(num.popleft())
	for val in num:
		while answer[-1] < val and garbage_num < k:
			answer.pop()
			garbage_num += 1
			if not answer:
				break
		answer.append(val)

	for cur in range(len(answer) - check_len):
		answer.pop()

	return ''.join(answer)


num = '4177252841'
k = 4

# num = '1231234'
# k = 3

# num = '77777'
# k = 2

print(solution(num, k))



