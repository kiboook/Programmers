from collections import deque


def solution(prices):
	answer = list()
	prices = deque(prices)

	while prices:
		check = prices.popleft()
		sec = 0

		for val in prices:
			sec += 1
			if check <= val:
				continue
			else:
				break
		answer.append(sec)

	return answer


prices = [1, 2, 3, 2, 3]
# prices = [4, 4, 3, 5, 5, 3, 2, 5]
print(solution(prices))