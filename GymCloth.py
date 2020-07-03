def giveAndTakeCloth(perDict, key, n):
	if key == 1:
		if perDict[key+1] == 2:
			perDict[key+1] -= 1
			perDict[key] += 1

	elif key == n:
		if perDict[key-1] == 2:
			perDict[key-1] -= 1
			perDict[key] += 1

	else:
		if perDict[key-1] == 2:
			perDict[key-1] -= 1
			perDict[key] += 1

		if perDict[key+1] == 2:
			perDict[key+1] -= 1
			perDict[key] += 1

def solution (n, lost, reserve):
	answer = 0
	perDict = {i+1:(1 if i+1 in reserve and i+1 in lost else 2 if i+1 in reserve else 0 if i+1 in lost else 1) for i in range(n)}

	for key, val in zip(perDict.keys(), perDict.values()):
		if val == 0:
			giveAndTakeCloth(perDict, key, n)

	for val in perDict.values():
		if val >= 1:
			answer += 1

	return answer

n = 6
lost = [1,3,5]
reserve = [2,4,6]

# n = 10
# lost = [4]
# reserve = [4]

print(solution(n, lost, reserve))