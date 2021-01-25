from itertools import combinations


def solution(orders, course):
	answer = list()

	for i in course:
		max_order_cnt = 0
		course_list = list()
		comb_list = list()

		for order in orders:
			comb_list.append(list(combinations(order, i)))

		comb_list = set(sum(comb_list, []))
		for val in comb_list:
			order_cnt = 0
			comb_food = set(val)

			for order in orders:
				if set.issubset(comb_food, order):
					order_cnt += 1

			if order_cnt >= 2:
				if max_order_cnt < order_cnt:
					course_list = [''.join(sorted(comb_food))]
					max_order_cnt = order_cnt
				elif max_order_cnt == order_cnt:
					course_list.append(''.join(sorted(comb_food)))

		answer += course_list

	return sorted(answer)


if __name__ == '__main__':
	orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
	course = [2, 3, 4]

	print(solution(orders, course))