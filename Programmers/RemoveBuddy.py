def solution(input_str):
	_stack = [input_str[0]]
	input_str = input_str[1:]
	for val in input_str:
		if _stack:
			if _stack[-1] == val:
				_stack.pop()
			else:
				_stack.append(val)
		else:
			_stack.append(val)

	if _stack:
		return 0
	else:
		return 1

my_str = 'baabaa'
# my_str = 'cvcv'
print(solution(my_str))


# def solution(input_str):
# 	idx = 0
# 	while idx < len(input_str) - 1:
# 		if input_str[idx] == input_str[idx + 1]:
# 			remove_str = input_str[idx] + input_str[idx + 1]
# 			input_str = input_str.replace(remove_str, '')
# 			idx = 0
# 			continue
# 		idx += 1
#
# 	if input_str:
# 		return 0
# 	else:
# 		return 1