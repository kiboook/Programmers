def solution(genres, plays):
	answer = []
	_dict = {i: [0, []] for i in set(genres)}

	for idx, song in enumerate(zip(genres, plays)):
		genre, play = song
		_dict[genre][0] += play
		_dict[genre][1].append([idx, play])

	for genre in _dict:
		# 재생횟수로 오름차순 정렬 후 고유 번호로 내림차순 정렬
		_dict[genre][1] = sorted(_dict[genre][1], key=lambda x: (x[1], -x[0]))

	song_list = []
	for genre in _dict:
		song_list.append([_dict[genre][0], genre])

	# 주어진 조건에 맞게 곡 선정
	song_list = sorted(song_list, reverse=True)
	print(_dict)
	print(song_list)
	for info in song_list:
		genre = info[1]
		pop_cnt = 0
		while _dict[genre][1]:
			answer.append(_dict[genre][1].pop()[0])
			pop_cnt += 1
			if pop_cnt == 2:
				break

	return answer


if __name__ == "__main__":
	genres = ["classic", "pop", "classic", "classic", "classic", "pop", "salsa"]
	plays = [500, 600, 150, 800, 500, 2500, 2000]

	print(solution(genres, plays))
