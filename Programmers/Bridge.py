from collections import deque


def check_add_truck(bridge, trucks, weight):
	total_weight = 0
	for cur in bridge:
		total_weight += cur[0]

	if trucks[0][0] + total_weight <= weight:
		return True
	else:
		return False


def solution(bridge_length, weight, truck_weights):
	trucks = deque([[val, 1] for val in truck_weights])
	bridge = deque()
	bridge.append(trucks.popleft())
	sec = 1

	while bridge:
		if bridge[-1][1] >= 2 and trucks:  # 다음 트럭이 들어 올 수 있나 확인
			if check_add_truck(bridge, trucks, weight):  # 들어 올 수 있는 경우
				bridge.append(trucks.popleft())
			else:
				pass

		for val in reversed(bridge):
			val[1] += 1
			if val[1] > bridge_length:
				bridge.popleft()

		if trucks and not bridge:  # bridge 가 비었고 truck 이 남아있는 경우
			bridge.append(trucks.popleft())
		sec += 1

	return sec


bridge_length = 5
weight = 10
truck_weights = [4, 3, 5, 9, 1]

# bridge_length = 100
# weight = 100
# truck_weights = [10]

# bridge_length = 2
# weight = 10
# truck_weights = [7, 4, 5, 6]

print(solution(bridge_length, weight, truck_weights))