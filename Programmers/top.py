from collections import deque


def solution(height):
	answer = []
	height_rev = deque(height[::-1])

	for loop in height:
		check = height_rev.popleft()
		for val in height_rev:
			if val > check:
				answer.append(len(height_rev) - height_rev.index(val))
				break
		else:
			answer.append(0)

	return answer[::-1]


height = [3, 9, 9, 3, 5, 7, 2]
# height = [6, 9, 5, 7, 4]
# height = [1, 5, 3, 6, 7, 6, 5]
# height = [9, 3, 9, 3]
print(solution(height))
