from itertools import permutations


def len_num(num):
	len = 0
	while num:
		len += 1
		num //= 10

	return len


def is_prime(num):
	result = False
	for i in range(2, num // 2 + 1):
		if num % i == 0:
			result = False
			break
	else:
		if num != 1:
			result = True

	return result


def solution(numbers):
	answer = 0
	_num = list(numbers)
	make_num = list()

	for idx in range(1, len(_num) + 1):
		tmp = [int(''.join(val)) for val in permutations(_num, idx) if len_num(int(''.join(val))) == idx]
		make_num.append(list(set(tmp)))

	for cur in make_num:
		for val in cur:
			if is_prime(val):
				answer += 1
			else:
				pass

	return answer


numbers = '017'
print(solution(numbers))

