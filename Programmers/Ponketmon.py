def solution(nums):
	return len(nums) // 2 if len(nums) // 2 < len(set(nums)) else len(set(nums))


def solution(nums):
	if len(nums) / 2 < len(set(nums)):
		answer = len(nums) // 2
	else:
		answer = len(set(nums))

	return answer


def solution(nums):
	return min(len(nums) // 2, len(set(nums)))


nums = [3, 1, 2, 3]
print(solution(nums))