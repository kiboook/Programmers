from math import ceil


def solution(n, a, b):
	round = 1

	while True:
		if max(a, b) - min(a, b) == 1 and max(a, b) % 2 == 0:
			break

		a = ceil(a / 2)
		b = ceil(b / 2)
		round += 1

	return round


N = 16
A = 8
B = 9
print(solution(N, A, B))