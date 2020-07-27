from collections import Counter


def solution(clothes):
	answer = 1
	clothes_cnt = [val[1] for val in clothes]
	clothes_dict = dict(Counter(clothes_cnt))

	for val in clothes_dict.values():
		answer *= val + 1

	return answer - 1


clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear'], ['crow_mask', 'face'], ['smoky_makeup', 'face'], ['qqqq', 'face'], ['vvv', 'eyewear']]
# clothes = [['crow_mask', 'face'], ['blue_sunglasses', 'faces'], ['smoky_makeup', 'facee']]
# clothes = [['crow_mask', 'face']]
print(solution(clothes))