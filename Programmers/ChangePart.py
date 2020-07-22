'''
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
  4-3. ')'를 다시 붙입니다.
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
  4-5. 생성된 문자열을 반환합니다.
'''


def make_u_v(p):  # 문자열 w를 두 '균형잡힌 괄호 문자열' u, v로 분리하는 함수
	left_cnt = 0
	right_cnt = 0

	for val in p:
		if val == '(':
			left_cnt += 1
		elif val == ')':
			right_cnt += 1

		if left_cnt == right_cnt:
			u = p[:left_cnt + right_cnt]
			v = p[left_cnt + right_cnt:len(p)]
			break

	return u, v


def is_collect(p):  # 올바른 괄호 문자열인지 여부를 반환하는 함수
	_stack = list()

	for val in p:
		try:
			if val == '(':
				_stack.append(val)
			elif val == ')':
				_stack.pop()
		except IndexError:
			return False

	if _stack:
		result = False
	else:
		result = True

	return result


def solution(p):
	if not p:
		return p

	u, v = make_u_v(p)
	if is_collect(u):
		return u + solution(v)
	else:
		tmp = '(' + solution(v) + ')'

		u = u[1:-1]
		u = u.replace('(', '0')
		u = u.replace(')', '1')
		u = u.replace('0', ')')
		u = u.replace('1', '(')

		return tmp + u


p = ')('
print(solution(p))
