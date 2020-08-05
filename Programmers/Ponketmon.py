def solution(nums):
	return len(nums) // 2 if len(nums) // 2 < len(set(nums)) else len(set(nums))


def solution(nums):
	half_len = len(nums) // 2
	set_len = len(set(nums))

	if half_len < set_len:
		answer = half_len
	else:
		answer = set_len

	return answer


def solution(nums):
	return min(len(nums) // 2, len(set(nums)))


nums = [3, 1, 2, 3]
print(solution(nums))