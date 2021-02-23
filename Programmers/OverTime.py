import heapq


def solution(n, works):
	result = 0

	if sum(works) <= n:
		return 0

	for i in range(len(works)):
		works[i] *= -1

	heapq.heapify(works)
	for i in range(n):
		work = heapq.heappop(works) * -1
		work -= 1
		heapq.heappush(works, work * -1)

	for work in works:
		result += (work ** 2)

	return result


if __name__ == '__main__':
	works = [2, 1, 2]
	n = 1
	print(solution(n, works))