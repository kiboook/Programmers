def solution(new_id):
	id = new_id
	id = id.lower()  # Step 1

	tmp_id = id[:]
	for idx in range(len(id)):  # Step 2
		if id[idx].islower() or id[idx].isdigit() or id[idx] in ['-', '_', '.']:
			continue
		else:
			tmp_id = tmp_id.replace(id[idx], '', 1)
	id = tmp_id[:]

	while True:  # Step 3
		tmp_id = id[:]
		id = id.replace("..", ".")
		if tmp_id == id:
			break

	if id and id[0] == '.':  # Step 4
		id = id[1:]
	if id and id[-1] == '.':
		id = id[:-1]

	if not id:  # Step 5
		id = 'a'

	if len(id) >= 16:  # Step 6
		id = id[:15]
		if id[-1] == '.':
			id = id[:-1]

	if len(id) <= 2:  # Step 7
		while len(id) <= 2:
			id += id[-1]

	return id


if __name__ == '__main__':
	new_id = input()
	print(solution(new_id))