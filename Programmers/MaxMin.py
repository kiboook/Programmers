def solution(s):
	_list = [int(val) for val in s.split(' ')]
	max_val = str(max(_list))
	min_val = str(min(_list))
	return min_val + ' ' + max_val


s = '-1 -2 -3 -4'
print(solution(s))