def solution(n, lost, reserve):

	# 여분을 가져 왔지만 잃어버린 사람 제외
	intersection = set(lost).intersection(set(reserve))
	lost = list(set(lost) - intersection)
	reserve = list(set(reserve) - intersection)

	lost_person = len(lost)
	for per in lost:
		if per - 1 in reserve:
			lost_person -= 1
			reserve.remove(per - 1)
			continue

		if per + 1 in reserve:
			lost_person -= 1
			reserve.remove(per + 1)
			continue

	return n - lost_person


if __name__ == '__main__':
	n = 5
	lost = [2, 4]
	reserve = [3]
	print(solution(n, lost, reserve))