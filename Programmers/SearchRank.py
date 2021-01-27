"""
정확성만 통과 한 코드.
효율성을 통과하려면 binary search 를 사용해야 한다.
"""


def solution(info, query):
	answer = list()

	info_set = list()
	for i in range(len(info)):
		split_info = info[i].split()
		tmp_list = list()

		tmp_list.append(set(split_info[:-1]))
		tmp_list.append(int(split_info[-1]))
		info_set.append(tmp_list)

	query_set = list()
	for i in range(len(query)):
		split_query = query[i].split(' ')
		tmp_list = list()
		tmp_set = set()

		for j in range(0, 7, 2):
			if split_query[j] != '-':
				tmp_set.add(split_query[j])
		tmp_list.append(tmp_set)
		tmp_list.append(int(split_query[-1]))
		query_set.append(tmp_list)

	for val in query_set:
		user_cnt = 0
		for user in info_set:
			if val[0].issubset(user[0]) and val[1] <= user[1]:
				user_cnt += 1
		answer.append(user_cnt)

	return answer


if __name__ == '__main__':
	_info = ["java backend junior pizza 150",
			"python frontend senior chicken 210",
			"python frontend senior chicken 150",
			"cpp backend senior pizza 260",
			"java backend junior chicken 80",
			"python backend senior chicken 50"]

	_query = ["java and backend and junior and pizza 100",
			 "python and frontend and senior and chicken 200",
			 "cpp and - and senior and pizza 250",
			 "- and backend and senior and - 150",
			 "- and - and - and chicken 100",
			 "- and - and - and - 150"]

	print(solution(_info, _query))