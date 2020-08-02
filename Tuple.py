# def solution(s):
# 	string = s[1:-1]
# 	sort_box = list()
# 	box = list()
# 	answer = list()
# 	input_num = ''
#
# 	for cur in string:
# 		if cur == '{':
# 			switch = True
# 			continue
# 		elif cur == '}':
# 			switch = False
# 			box.append(int(input_num))
# 			sort_box.append(box.copy())
# 			box.clear()
# 			input_num = ''
#
# 		if switch and cur != ',':
# 			input_num += cur
#
# 		if switch and cur == ',':
# 			box.append(int(input_num))
# 			input_num = ''
#
# 	sort_box.sort(key=lambda x: len(x))
# 	answer.append(sort_box[0][0])
#
# 	for val in sort_box:
# 		answer += set(val) - set(answer)
#
# 	return answer


def solution(s):
	split_str = s[2:-2].split('},{')
	sort_box = []
	box = []
	answer = []
	input_num = ''

	for cur in split_str:
		for val in cur:
			if val != ',':
				input_num += val
			else:
				box.append(int(input_num))
				input_num = ''

		box.append(int(input_num))
		input_num = ''
		sort_box.append(box.copy())
		box.clear()

	sort_box.sort(key=lambda x: len(x))

	for val in sort_box:
		answer += set(val) - set(answer)

	return answer


# s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
# s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
s = "{{20,111},{111}}"
print(solution(s))