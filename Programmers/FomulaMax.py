from itertools import permutations as per
from copy import deepcopy


def solution(string):
	cal = ['-', '+', '*']
	priority = list(map(list, per(cal)))
	input_list = []
	answer = []

	tmp = ''
	for cur in string:
		if cur in cal:
			input_list.append(int(tmp))
			input_list.append(cur)
			tmp = ''
		else:
			tmp += cur
	input_list.append(int(tmp))

	for cur in priority:
		tmp_list = deepcopy(input_list)
		for cal in cur:
			idx = 0
			while idx < len(tmp_list):
				if tmp_list[idx] == cal:
					if tmp_list[idx] == '-':
						tmp = tmp_list[idx - 1] - tmp_list[idx + 1]
					elif tmp_list[idx] == '+':
						tmp = tmp_list[idx - 1] + tmp_list[idx + 1]
					elif tmp_list[idx] == '*':
						tmp = tmp_list[idx - 1] * tmp_list[idx + 1]
					tmp_list[idx - 1] = tmp
					tmp_list.pop(idx)
					tmp_list.pop(idx)
					idx -= 1

				idx += 1
		answer.append(abs(tmp_list[0]))
	return max(answer)


# my_str = '100-200*300-500+20'
my_str = '50*6-3*2'
# my_str = '100-90-80+10+20+30'
print(solution(my_str))