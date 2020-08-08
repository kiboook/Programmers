# import numpy as np
#
#
# def solution(arr1, arr2):
# 	result = []
#
# 	for cur in list(np.dot(arr1, arr2)):
# 		result.append(list(cur))
#
# 	return result

def solution(arr1, arr2):
	spin_arr2 = []
	result = []

	for i in range(len(arr2[0])):
		tmp = []
		for j in range(len(arr2)):
			tmp.append(arr2[j][i])
		spin_arr2.append(tmp)

	for cur1 in arr1:
		tmp = []
		for cur2 in spin_arr2:
			tmp_val = 0
			for val1, val2 in zip(cur1, cur2):
				tmp_val += val1 * val2
			tmp.append(tmp_val)
		result.append(tmp)

	return result


arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1, arr2))