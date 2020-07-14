def check_answer(answers, checkList, checkCnt):

	for index,value in enumerate(answers):
		if checkList[index % len(checkList)] == value:
			checkCnt += 1
	return checkCnt

def solution(answers):
	answer = []
	answerCnt = []

	one = [1, 2, 3, 4, 5]
	two = [2, 1, 2, 3, 2, 4, 2, 5]
	three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

	oneCnt = twoCnt = threeCnt = 0
	answerCnt.append(check_answer(answers, one, oneCnt))
	answerCnt.append(check_answer(answers, two, twoCnt))
	answerCnt.append(check_answer(answers, three, threeCnt))

	for index, value in enumerate(answerCnt):
		if max(answerCnt) == value:
			answer.append(index+1)

	return answer


answers = [1, 2, 3, 4, 5]
print(solution(answers))