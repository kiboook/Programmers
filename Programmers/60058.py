def is_collect(u):
	stack = []
	for i in u:
		if i == '(':
			stack.append('(')
		if i == ')':
			try:
				stack.pop()
			except IndexError:
				return False
	if stack:
		return False
	return True


def split_U_V(p):
	u, v = '', ''

	left, right = 0, 0
	for i in p:
		if i == '(':
			left += 1
		elif i == ')':
			right += 1

		if left == right:
			return p[:left * 2], p[left * 2:]


def solution(p):
	if not p:
		return p

	u, v = split_U_V(p)
	if is_collect(u):
		return u + solution(v)
	else:
		empty = '(' + solution(v) + ')'
		u = u[1:-1]
		u = u.replace('(', '0')
		u = u.replace(')', '1')
		u = u.replace('0', ')')
		u = u.replace('1', '(')

	return empty + u


if __name__ == '__main__':
	p = input()
	print(solution(p))