def solution(brown, yellow):
	answer = list()
	yellow_divisor = list()
	for i in reversed(range(1, yellow + 1)):
		if yellow % i == 0:
			if int(yellow / i) <= i:
				yellow_divisor.append([i, int(yellow / i)])
			else:
				break

	for weight, height in yellow_divisor:
		brown_cnt = 0
		while brown_cnt < brown:
			brown_cnt = (weight + height) * 2 + 4
			weight += 2
			height += 2

			if brown_cnt == brown:
				answer += [weight, height]
				return answer


brown = 8
yellow = 1
print(solution(brown, yellow))