# def solution(array, commands):
# 	answer = []

# 	for val in commands:
# 		i = val[0]
# 		j = val[1]
# 		k = val[2]

# 		temp = array[i-1:j]
# 		temp.sort()

# 		answer.append(temp[k-1])

# 	return answer

# def solution(array, commands):
# 	answer = []

# 	for val in commands:
# 		i, j, k = val
# 		temp = list(sorted(array[i-1:j]))

# 		answer.append(temp[k-1])

# 	return answer

def solution(array, commands):
	answer = []

	for val in commands:
		i, j, k = val

		answer.append(list(sorted(array[i-1:j]))[k-1])

	return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))

