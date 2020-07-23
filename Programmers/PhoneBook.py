import time
from collections import deque


def solution(phone_book):
	sort_phone = deque(sorted(phone_book))

	while sort_phone:
		val_min = sort_phone.popleft()
		for val in sort_phone:
			if val_min == val[:len(val_min)]:
				return False

	return True


# phone_book = ['3213', '213', '7979', '21397']
# phone_book = ['12', '123', '1235', '567', '88']
# phone_book = ['123', '456', '789']
# phone_book = ['213', '2153', '215353']
# phone_book = ['13', '12', '11', '1991324', '199', '16', '17', '18']

phone_book = [str(val) for val in range(10000)]
start = time.time()
print(solution(phone_book))
print(time.time() - start)
