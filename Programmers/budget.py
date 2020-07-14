def solution(d, budget):
	answer = 0
	dSum = 0
	d.sort() # 가격 정렬

	for cur in d:
		dSum += cur
		if dSum <= budget:
			answer += 1
		else:
			break;
	return answer