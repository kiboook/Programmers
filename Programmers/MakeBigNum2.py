def solution(nums):
	answer = ''.join(sorted(map(str, nums), key=lambda x: x * 3, reverse=True))
	if answer[0] == '0':
		answer = '0'

	return answer


numbers = [2, 3, 5, 0, 1]
print(solution(numbers))