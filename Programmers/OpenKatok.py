def solution(record):
	user = dict()
	answer = list()

	for cur in record:
		order = cur.split(' ')
		if order[0] == 'Enter':
			user[order[1]] = order[2]
		elif order[0] == 'Change':
			user[order[1]] = order[2]

	for cur in record:
		order = cur.split(' ')
		if order[0] == 'Enter':
			answer.append(user[order[1]] + '님이 들어왔습니다.')
		elif order[0] == 'Leave':
			answer.append(user[order[1]] + '님이 나갔습니다.')

	return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(record))