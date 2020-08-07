# def solution(A, B):
# 	result = 0
#
# 	while len(A) > 0:
# 		result += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))
#
# 	return result

def solution(A, B):
	result = 0

	for val_A, val_B in zip(sorted(A), sorted(B, reverse=True)):
		result += val_A * val_B

	return result


A = [3, 4, 6]
B = [8, 2, 1]
print(solution(A, B))