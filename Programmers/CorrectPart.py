# def solution(s):
# 	stack = list()
#
# 	for cur in s:
# 		try:
# 			if cur == '(':
# 				stack.append(cur)
# 			elif cur == ')':
# 				stack.pop()
# 		except IndexError:
# 			return False
#
# 	return len(stack) == 0

# def solution(s):
# 	stack = list()
# 	answer = True
#
# 	for cur in s:
# 		try:
# 			if cur == '(':
# 				stack.append(cur)
# 			elif cur == ')':
# 				stack.pop()
# 		except IndexError:
# 			answer = False
#
# 	if len(stack) > 0:
# 		answer = False
#
# 	return answer

def solution(s):
	stack = list()
	answer = True

	for cur in s:
		try:
			if cur == '(':
				stack.append(cur)
			elif cur == ')':
				stack.pop()
		except IndexError:
			return False

	if len(stack) > 0:
		answer = False

	return answer

s = '(())())('
print(solution(s))