def solution(land):
	dp = land.copy()
	for idx in range(1, len(land)):
		dp[idx][0] += max(dp[idx - 1][1], dp[idx - 1][2], dp[idx - 1][3])
		dp[idx][1] += max(dp[idx - 1][0], dp[idx - 1][2], dp[idx - 1][3])
		dp[idx][2] += max(dp[idx - 1][0], dp[idx - 1][1], dp[idx - 1][3])
		dp[idx][3] += max(dp[idx - 1][0], dp[idx - 1][1], dp[idx - 1][2])

	return max(dp[len(dp) - 1])


# land = [[7, 7, 60, 100], [50, 10, 5, 100], [4, 7, 2, 300], [10, 2, 5, 900]]
land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
# land = [[1, 2, 3, 4], [5, 6, 7, 9], [4, 3, 2, 1]]
print(solution(land))