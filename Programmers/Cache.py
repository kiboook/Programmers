from collections import deque


def solution(cacheSize, cities):
	total = 0
	cache = deque()
	cities = [val.title() for val in cities]

	if cacheSize == 0:
		return len(cities) * 5

	for idx, val in enumerate(cities):
		if len(cache) < cacheSize:
			if val in cache:
				total += 1
			else:
				cache.append(val)
				total += 5
		elif len(cache) == cacheSize:
			if val in cache:
				total += 1
			else:
				lately_used = []
				lately_idx = idx - 1
				while len(lately_used) < cacheSize - 1:
					if cities[lately_idx] not in lately_used:
						lately_used.append(cities[lately_idx])
					lately_idx -= 1

				chance_val = ''
				for j in cache:
					if j not in lately_used:
						chance_val = j

				input_idx = cache.index(chance_val)
				cache.insert(input_idx, val)
				cache.remove(chance_val)
				total += 5

	return total


cacheSize = 3
# cities = ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']
cities = ["Jeju", "Jeju", "Pangyo", "Seoul", "NewYork", "newyork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(cacheSize, cities))