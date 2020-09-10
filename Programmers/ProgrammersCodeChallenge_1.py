# 프로그래머스 코딩 챌린지 시즌 1 1번 #

def solution1(numbers):
	answer = set()
	for i in range(len(numbers) - 1):
		for j in range(i + 1, len(numbers)):
			answer.add(numbers[i] + numbers[j])

	return sorted(list(answer))


numbers = [2, 1, 3, 4, 1]
print(solution1(numbers))

# 프로그래머스 코딩 챌린지 시즌 1 2번 #

# def solution(n):
# 	answer = []
# 	box = [[] for i in range(n)]
#
#
#
# 	return answer
#
#
# n = 6
# print(solution(n))

# 프로그래머스 코딩 챌린지 시즌 1 3번 #
def solution3(a):
	left_min = [a[0]]
	right_min = [a[len(a) - 1]]

	min = left_min[0]
	for i in range(1, len(a)):
		if a[i] < min:
			min = a[i]

		left_min.append(min)

	min = right_min[0]
	for i in reversed(range(1, len(a))):
		if a[i] < min:
			min = a[i]

		right_min.append(min)

	right_min = right_min[::-1]

	answer = len(a)
	for i in range(len(a)):
		if left_min[i] < a[i] and right_min[i] < a[i]:
			answer -= 1

	return answer


a = [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]
print(solution3(a))

# 프로그래머스 코딩 챌린지 시즌 1 4번 #