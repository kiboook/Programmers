def solution(participant, completion):
	answer = dict()

	for cur in participant:
		answer[cur] = 0

	for cur in participant:
		answer[cur] += 1

	for cur in completion:
		answer[cur] -= 1

	for cur in answer:
		if answer[cur] == 1:
			return cur


participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']

# participant = ['mislav', 'stanko', 'mislav', 'ana']
# completion = ['stanko', 'ana', 'mislav']

# participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
# completion = ['josipa', 'filipa', 'marina', 'nikola']	

print(solution(participant, completion))