import heapq as hq


def solution(stock, dates, supplies, k):
	answer = 0
	start = 0
	max_supply = []
	flour_sum = stock

	while flour_sum < k:  # 밀가루가 k개 미만인 경우 보급받는다.
		for idx in range(start, len(dates)):
			if dates[idx] <= flour_sum:  # 보급 받을 수 있는 날 까지 보급량을 최대힙에 넣어준다.
				hq.heappush(max_supply, -supplies[idx])

			else:  # 보급 받을 수 있는 날 보다 먼저 받을 수 없으니 종료
				break

		start = idx  # 이미 힙에 넣어준 공급량을 중복해서 넣지 않도록 start 를 수정해준다.
		flour_sum += -hq.heappop(max_supply)
		answer += 1

	return answer


# stock = 3
# dates = [1]
# supplies = [50]
# k = 13

stock = 4
dates = [4, 10, 15]
supplies = [20, 5, 10]
k = 30

print(solution(stock, dates, supplies, k))

