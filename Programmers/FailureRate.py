import operator

def solution(N, stages):
	answer = []
	temp = dict()

	for i in range(N):
		curStage = 0
		overStage = 0

		for j in stages:
			if i+1 == j:
				curStage += 1
			
			if i+1 <= j:
				overStage += 1

		if curStage == 0 or overStage == 0:
			temp[i+1] = 0
		else:
			temp[i+1] = curStage / overStage
		
	sTemp = sorted(temp.items(), key=operator.itemgetter(1), reverse=True)
	
	for cur in sTemp:
		answer.append(cur[0])

	return answer



N = 5
stages = [2,1,2,6,2,4,3,3]
print(solution(N, stages))