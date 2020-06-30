def solution(dartResult):
	answer = 0
	checkNum = ['0','1','2','3','4','5','6','7','8','9','k']
	dartList = []
	dartScore = []
	dartResult = dartResult.replace('10', 'k')

	
	while len(dartResult) > 3: # dart 명령 분리
		orderCount = 0
		for index in range(1, len(dartResult)):
			if dartResult[index] not in checkNum:
				orderCount += 1
			else:
				break
		dartList.append(dartResult[:orderCount+1])
		dartResult = dartResult.replace(dartResult[:orderCount+1],'')
	dartList.append(dartResult)

	for i in range(3):
		for j in range(len(dartList[i])):
			if dartList[i][j] in checkNum:
				try:
					dartScore.append(int(dartList[i][j]))
				except:
					dartScore.append(10)

			elif dartList[i][j] == 'D':
				dartScore[i] = dartScore[i] ** 2

			elif dartList[i][j] == 'T':
				dartScore[i] = dartScore[i] ** 3

			elif dartList[i][j] == '*':
				if i == 0:
					dartScore[i] *= 2
				else:
					dartScore[i-1] *= 2
					dartScore[i] *= 2

			elif dartList[i][j] == '#':
				dartScore[i] *= -1

	return sum(dartScore)



dartResult = '1S*2T*3S'
# dartResult = '4D2S3D'
# dartResult = '1S2D*3T'
# dartResult = '1S2D*3T'
# dartResult = '1S2D*3T'

print(solution(dartResult))



