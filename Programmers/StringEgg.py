def solution(s):
	if len(s) == 1:
		return 1

	answer = ''
	len_list = []

	for i in range(1, (len(s) // 2) + 1):
		output = ''
		cnt = 0
		check = s[0:i]
		for j in range(0, len(s) + 1, i):
			if check == s[j:j+i]:
				cnt += 1
			else:
				if cnt == 1:
					output += check
				else:
					output += (str(cnt) + check)
				check = s[j:j+i]
				cnt = 1
		output += s[j:len(s)]  # 다 계산 후 남은 부분 채워주기
		print(output)
		len_list.append(len(output))

	return min(len_list)


s = 'ababcdcdababcdcd'
# s = 'aabbaabb'
# s = 'a'

print(solution(s))