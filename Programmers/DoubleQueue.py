import heapq
import bisect


def solution(operations):
	min_heap = []
	max_heap = []

	for operation in operations:
		order, num = operation.split()
		if order == "I":
			heapq.heappush(min_heap, int(num))
			heapq.heappush(max_heap, int(num) * -1)

		if order == "D":
			if max_heap and min_heap:
				if num == '-1':
					# 최소힙 삭제 후 최대힙 동기화
					idx = bisect.bisect(max_heap, heapq.heappop(min_heap) * -1) - 1
					max_heap.pop(idx)

				if num == '1':
					# 최대힙 삭제 후 최소힙 동기화
					idx = bisect.bisect(min_heap, heapq.heappop(max_heap) * -1) - 1
					min_heap.pop(idx)

	if max_heap and min_heap:
		return [max_heap[0] * -1, min_heap[0]]
	else:
		return [0, 0]


if __name__ == '__main__':
	operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
	print(solution(operations))