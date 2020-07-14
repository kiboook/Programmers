# def solution(a, b):
# 	day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
# 	year = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

# 	checkDay = 0
# 	for idx in range(1,a):
# 		checkDay += year[idx]
# 	checkDay += b

# 	print(checkDay)
# 	return day[(checkDay%7)-1]

# a = 1
# b = 1
# print(solution(a,b))


from string import ascii_lowercase
from string import ascii_uppercase

def solution(s, n):

	lower = list(ascii_lowercase)
	upper = list(ascii_uppercase)

	answer = ''
	for val in s:
		if val in lower:
			answer += lower[(lower.index(val)+n)%len(lower)]
		elif val in upper:
			answer += upper[(upper.index(val)+n)%len(upper)]
		else:
			answer += val

	return answer

s = 'az'
n = 1
print(solution(s,n))







