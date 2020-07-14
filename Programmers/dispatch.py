from math import ceil
from collections import deque



def solution(progresses, speed):
	answer = []
	date = [ceil((100 - p) / s) for p, s in zip(progresses, speed)]

	while date:
		cnt = 1
		check = date.pop(0)

		while True:
			try:
				if check >= date[0]:
					date.pop(0)
					cnt += 1
				else:
					answer.append(cnt)
					break

			except IndexError:
				answer.append(cnt)
				break
	return answer


progresses = [93, 30, 55]
speed = [1, 30, 5]

print(solution(progresses, speed))
