answer = 0


def DFS(nums, target, idx, sum):
	global answer
	if idx == len(nums):
		if sum == target:
			answer += 1
		return

	DFS(nums, target, idx + 1, sum + nums[idx])
	DFS(nums, target, idx + 1, sum - nums[idx])


def solution(nums, target):
	DFS(nums, target, 0, 0)
	return answer


# nums = [1, 1, 2, 1, 2, 1]
# target = 4
nums = [1, 1, 1, 1, 1]
target = 3
print(solution(nums, target))