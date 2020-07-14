def solution(n, arr1, arr2):
	answer = [''for i in range(n)]
	
	bitCal = []
	for i in range(len(arr1)):
		bitCal.append(bin(arr1[i]|arr2[i])[2:])
	print(bitCal)

	index = 0
	for cur in bitCal:
		
		inputMap = ''
		for i in range(len(cur)):
			if cur[i] == '1':
				inputMap += '#'
			elif cur[i] == '0':
				inputMap += ' '

		if len(inputMap) != n:
			extraSpace = ''
			for i in range(n-len(inputMap)):
				extraSpace += ' '
			inputMap = extraSpace + inputMap
		answer[index] = inputMap
		index += 1

	return answer

def solution2(n, arr1, arr2):
	answer = []

	for i, j in zip(arr1, arr2):
		bitCal = bin(i|j)[2:]
		
		bitCal = bitCal.rjust(n, '0')
		bitCal = bitCal.replace('1', '#')
		bitCal = bitCal.replace('0', ' ')
		answer.append(bitCal)

	return answer


# n = 5
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

# n = 6
# arr1 = [46, 33, 33 ,22, 1, 50]
# arr2 = [27 ,56, 19, 14, 4, 10]





 




