def solution(baseball):
	answer = 0

	for check_num in range(123, 999):
		check_num = str(check_num)
		if '0' in check_num or len(set(list(check_num))) < 3:  # 숫자에 0이 있거나 중복 된 숫자가 있으면 넘어간다
			continue

		answer_check = 0
		for cur in baseball:
			strike = 0
			ball = 0
			answer_num = str(cur[0])
			for val in check_num:
				try:
					if check_num.index(val) == answer_num.index(val):
						strike += 1
					else:
						ball += 1
				except ValueError:
					pass

			if cur[1] == strike and cur[2] == ball:
				answer_check += 1
			else:
				pass

		if answer_check == len(baseball):
			print(check_num)
			answer += 1

	return answer


baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print(solution(baseball))