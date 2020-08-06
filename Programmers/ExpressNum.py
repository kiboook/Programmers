def solution(num):
	answer = 0

	for n in range(1, num + 1):
		check = n

		k = 1
		while check < num:
			check = k * n + k * (k - 1) / 2
			k += 1

		if check == num:
			answer += 1

	return answer


num = 15
print(solution(num))