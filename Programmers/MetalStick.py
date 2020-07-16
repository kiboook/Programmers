# def solution(arr):
# 	answer = 0
# 	arr = arr.replace('()', 'L')
# 	stick = list()
#
# 	for val in arr:
# 		if val == '(':
# 			stick.append(0)
# 		elif val == ')':
# 			input = stick.pop() + 1
# 			answer += input
#
# 		elif val == 'L':
# 			for idx, cnt in enumerate(stick):
# 				stick[idx] = cnt + 1
#
# 	answer += input
# 	return answer

def solution(arr):
	arr = arr.replace('()', 'L')
	answer = 0
	open = list()

	for val in arr:
		if val == '(':
			open.append(val)
		elif val == ')':
			answer += 1
			open.pop()
		elif val == 'L':
			answer += len(open)

	return answer

arr = '()(((()())(())()))(())'
print(solution(arr))