def get_time(start, end):
	start_time = start.split(':')
	start_h = int(start_time[0])
	start_m = int(start_time[1])

	end_time = end.split(':')
	end_h = int(end_time[0])
	end_m = int(end_time[1])

	if start_m <= end_m:  # 시작 분 보다 종료 분이 더 크거나 같 경우, 작은 경우
		runtime = (end_h - start_h) * 60 + (end_m - start_m)
	else:
		runtime = (end_h - start_h - 1) * 60 + (60 - start_m) + end_m

	return runtime


def solution(m, musicinfos):
	song = dict()
	info = [val.split(',') for val in musicinfos]  # 시작시간, 종료시간, 노래이름, 멜로디로 나누기
	m = m.replace('C#', '$')  #  #이 붙은 멜로디는 계산하기 편하게 치환한다
	m = m.replace('D#', '%')
	m = m.replace('F#', '^')
	m = m.replace('G#', '&')
	m = m.replace('A#', '*')

	for val in info:
		val[3] = val[3].replace('C#', '$')
		val[3] = val[3].replace('D#', '%')
		val[3] = val[3].replace('F#', '^')
		val[3] = val[3].replace('G#', '&')
		val[3] = val[3].replace('A#', '*')

		runtime = get_time(val[0], val[1])
		melody = ''
		for idx in range(runtime):  #  재생 시간만큼 멜로디를 담는다
			melody += val[3][idx % len(val[3])]
		song[val[2]] = melody

	answer = list()
	for val in song.items():  # 찾고자 하는 음악을 모두 담는다
		if m in val[1]:
			answer.append([val[0], len(val[1])])

	if len(answer) == 0:  #  찾고자 하는 음악이 없는 경우, 한 개인 경우, 여러 개인 경우 조건
		return '(None)'

	elif len(answer) == 1:
		return answer[0][0]

	else:
		longest = max([val[1] for val in answer])
		for val in answer:
			if longest == val[1]:
				return val[0]

m = 'ABCDEFG'
musicinfos = ['12:00,12:14,HELLO,CDEFGAB', '13:00,14:20,WORLDEST,ABCDEFG']  # WORDEST 출력

# m = 'CC#BCC#BCC#BCC#B'
# musicinfos = ['03:00,00:00,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']

# m = 'ABCDEFG'은
# musicinfos = ['12:00,13:20,HELLO,CDEFGAB', '13:00,14:20,WORLDEST,ABCDEFG']  # HELLO 출력

print(solution(m, musicinfos))
