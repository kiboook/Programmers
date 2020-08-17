from itertools import combinations


def solution(relation):
	attribute = list(map(list, zip(*relation)))
	candidate = []

	for i in range(1, len(attribute) + 1):
		attribute_num = map(list, combinations([val for val in range(len(attribute))], i))
		for j in attribute_num:
			check = []
			for k in j:
				check.append(attribute[k])
			if len(set(zip(*check))) == len(attribute[0]):
				for cur in candidate:
					if cur.issubset(set(j)):
						break
				else:
					candidate.append(set(j))

	return len(candidate)

relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
			["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
print(solution(relation))
