import heapq


def solution(scoville, k):
	answer = 0
	min_heap = list()

	for val in scoville:
		heapq.heappush(min_heap, val)

	while True:
		try:
			num1 = heapq.heappop(min_heap)
			num2 = heapq.heappop(min_heap)
			num3 = num1 + (num2 * 2)
			heapq.heappush(min_heap, num3)
			answer += 1

		except IndexError:
			answer = -1
			break

		if min_heap[0] >= k:
			break

	return answer


scoville = [7, 4, 10, 2, 5]
k = 7
print(solution(scoville, k))