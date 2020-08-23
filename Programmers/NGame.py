def change_num(num, n):
	output = ''
	if num == 0:
		output = '0'

	while num:
		if num % n == 10:
			output += 'A'
		elif num % n == 11:
			output += 'B'
		elif num % n == 12:
			output += 'C'
		elif num % n == 13:
			output += 'D'
		elif num % n == 14:
			output += 'E'
		elif num % n == 15:
			output += 'F'
		else:
			output += str(num % n)
		num = int(num / n)

	return output[::-1]


def solution(n, t, m, p):
	answer = ''
	start = 0
	turn = 1
	while True:
		change = change_num(start, n)
		for i in change:
			if turn == p:
				answer += i
				p += m
				if len(answer) == t:
					return answer
			turn += 1
		start += 1


n, t, m, p = 16, 16, 2, 2
print(solution(n, t, m, p))