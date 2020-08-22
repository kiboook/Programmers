import re


def solution(files):
	head = []
	num = []
	tail = []

	for cur in files:
		head_input = num_input = tail_input = ''
		for val in cur:
			if len(head_input) > 0 and len(num_input) > 0:
				if re.match('[^0-9]', val):
					break

			if re.match('[^0-9]', val):
				head_input += val
			else:
				num_input += val

		head.append(head_input)
		num.append(num_input)
		tail.append(cur[len(head_input) + len(num_input):len(cur)])

	_split = list(zip(head, num, tail))
	box = sorted(_split, key=lambda file: (file[0].upper(), int(file[1])))
	answer = []
	for val in box:
		answer.append(''.join(val))

	return answer


# files = ['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']
files = ['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']
# files = ['foo9.txt', 'foo010bar020.zip', 'F-15']
print(solution(files))