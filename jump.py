import math

def solution(n):
    ans = 0

    # n을 1이 될때 까지 2로 나누고 값이 홀수이면 버림하고 ans를 1 올린다.
    while n >= 1:
    	if n % 2 == 0:
    		n = n/2
    	else:
    		n = math.floor(n/2)
    		ans += 1
    return ans


n=5000
print(solution(n))

