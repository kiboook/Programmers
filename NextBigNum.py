def solution(num):
	num_one_cnt = bin(num)[2:].count('1')

	for val in range(num + 1, 1000001):
		if num_one_cnt == bin(val)[2:].count('1'):
			return val


num = 185892
print(solution(num))