from string import ascii_uppercase


def solution(msg):
	answer = list()
	_dict = dict()
	for val in ascii_uppercase:
		_dict[val] = len(_dict) + 1

	while msg:
		w = ''
		for idx in range(len(msg)):
			if msg[:idx + 1] in _dict:
				w = msg[:idx + 1]
			else:
				break

		answer.append(_dict[w])
		msg = msg[len(w):]
		if msg:
			wc = w + msg[0]
			_dict[wc] = len(_dict) + 1

	return answer


msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))
