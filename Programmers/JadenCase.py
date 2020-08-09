def solution(s):

	box = list(s.split(' '))
	
	for idx, val in enumerate(box):
		box[idx] = val.capitalize()

	return ' '.join(box)


s = '3people unFollowed me'
s = 'cBgiEb IlxDFS vCSL  Bz'
print(solution(s))