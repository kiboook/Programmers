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
				dartScore[i] *= 2
				if i != 0:
					dartScore[i-1] *= 2

			elif dartList[i][j] == '#':
				dartScore[i] *= -1

	return sum(dartScore)


dartResult = '10S*2T*3S'
# dartResult = '4D2S3D'
# dartResult = '1S2D*3T'
# dartResult = '1S2D*3T'
# dartResult = '1S2D*3T'

print(solution(dartResult))


# def solution(dartResult): 정규화 안 쓰고 나누어서 한 코드인데 진짜 신기..
#     point = []
#     answer = []
#     dartResult = dartResult.replace('10','k')
#     point = ['10' if i == 'k' else i for i in dartResult]
#     print(point)

#     i = -1
#     sdt = ['S', 'D', 'T']
#     for j in point:
#         if j in sdt :
#             answer[i] = answer[i] ** (sdt.index(j)+1)
#         elif j == '*':
#             answer[i] = answer[i] * 2
#             if i != 0 :
#                 answer[i - 1] = answer[i - 1] * 2
#         elif j == '#':
#             answer[i] = answer[i] * (-1)
#         else:
#             answer.append(int(j))
#             i += 1
#     return sum(answer)

