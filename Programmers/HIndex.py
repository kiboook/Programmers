def solution(citation):
	h = 0
	for citation_num in range(max(citation) + 1):
		cnt = 0

		for val in citation:
			if citation_num <= val:
				cnt += 1

		if citation_num <= cnt:
			h = citation_num

	return h


# citation = [3, 0, 6, 1, 5]
citation = [3, 3, 3, 3]
# citation = [25, 8, 5, 3, 3]
print(solution(citation))