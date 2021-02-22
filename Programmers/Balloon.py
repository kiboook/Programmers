def solution(a):
	answer = 0
	left, right = a[0], a[-1]
	left_min, right_min = [0] * len(a), [0] * len(a)

	for i in range(len(a)):
		if a[i] < left:
			left = a[i]
		left_min[i] = left

	for i in reversed(range(len(a))):
		if a[i] < right:
			right = a[i]
		right_min[i] = right

	for i in range(len(a)):
		if left_min[i] >= a[i] or right_min[i] >= a[i]:
			answer += 1

	return answer


if __name__ == '__main__':
	a = [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]
	print(solution(a))