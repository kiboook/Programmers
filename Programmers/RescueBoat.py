def solution(people, limit):
	answer = 0
	people = sorted(people)

	left_idx = 0
	right_idx = len(people) - 1

	while left_idx <= right_idx:
		if people[left_idx] + people[right_idx] <= limit:
			left_idx += 1
			right_idx -= 1
			answer += 1
		else:
			right_idx -= 1
			answer += 1

	return answer

# people = [70, 20, 10, 20, 50, 90, 100, 100, 100, 100]
people = [10, 100, 100, 100, 100]
# people = [70, 80, 50, 40, 40, 40, 40]
# people = [100, 100, 100, 100, 100, 100, 40, 90]
limit = 100
print(solution(people, limit))