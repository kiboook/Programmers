from string import ascii_uppercase
from copy import deepcopy

def solution(A, B):
	alpha = ascii_uppercase
	A = A.upper()
	B = B.upper()
	A_set = []
	B_set = []

	for idx in range(len(A) - 1):
		if A[idx] in alpha and A[idx + 1] in alpha:
			A_set.append(A[idx] + A[idx + 1])

	for idx in range(len(B) - 1):
		if B[idx] in alpha and B[idx + 1] in alpha:
			B_set.append(B[idx] + B[idx + 1])

	if len(A_set) == 0 and len(B_set) == 0:
		return 65536

	same_cnt = 0
	if len(A_set) <= len(B_set):
		for val in deepcopy(A_set):
			if val in B_set:
				same_cnt += 1
				A_set.remove(val)
				B_set.remove(val)
	else:
		for val in deepcopy(B_set):
			if val in A_set:
				same_cnt += 1
				A_set.remove(val)
				B_set.remove(val)

	all_cnt = len(A_set) + len(B_set) + same_cnt
	answer = int(same_cnt / all_cnt * 65536)
	return answer



str1 = 'abdsflkjharbqwhlfhqgk'
str2 = 'a+b+c+d'

# str1 = 'frAnce'
# str2 = 'FrenCh'

# str1 = 'E=M*C^2'
# str2 = 'e=m*c^2'

# str1 = '+@+!$!@+'
# str2 = '+@$!51s'

print(solution(str1, str2))