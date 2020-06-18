from itertools import combinations

def isPrime(num):
	for i in range(2,num):
		if(num % i == 0):
			return False

	return True

def solution(nums):
	answer = 0
	comb = list(combinations(nums, 3))

	for i in comb:
		if(isPrime(sum(i))):
			answer += 1

	return answer

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,]
print(solution(nums))
