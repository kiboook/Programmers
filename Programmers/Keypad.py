# def solution(numbers, hand):
# 	for index, value in enumerate(numbers):
# 		if value == 0:
# 			numbers[index] = 11

# 	answer = ''
# 	curLeft = 10
# 	curRight = 12

# 	left = [1, 4, 7]
# 	center = [2, 5, 8, 11]
# 	right = [3, 6, 9]

# 	for finger in numbers:

# 		if finger in left:
# 			answer += 'L'
# 			curLeft = finger

# 		elif finger in right:
# 			answer += 'R'
# 			curRight = finger

# 		elif finger in center:

# 			leftDistance = abs(finger - curLeft)
# 			rightDistance = abs(finger - curRight)

# 			if leftDistance == 1 or leftDistance == 3:
# 				leftDistance = 1
# 			elif leftDistance == 2 or leftDistance == 4 or leftDistance == 6:
# 				leftDistance = 2
# 			elif leftDistance == 5 or leftDistance == 7 or leftDistance == 9:
# 				leftDistance = 3
# 			elif leftDistance == 8 or leftDistance == 10:
# 				leftDistance = 4

# 			if rightDistance == 1 or rightDistance == 3:
# 				rightDistance = 1
# 			elif rightDistance == 2 or rightDistance == 4 or rightDistance == 6:
# 				rightDistance = 2
# 			elif rightDistance == 5 or rightDistance == 7 or rightDistance == 9:
# 				rightDistance = 3
# 			elif rightDistance == 8 or rightDistance == 10:
# 				rightDistance = 4

# 			if leftDistance < rightDistance:
# 				answer += 'L'
# 				curLeft = finger
# 			elif leftDistance > rightDistance:
# 				answer += 'R'
# 				curRight = finger
# 			elif leftDistance == rightDistance:
# 				if hand == 'right':
# 					answer += 'R'
# 					curRight = finger
# 				elif hand == 'left':
# 					answer += 'L'
# 					curLeft = finger

# 	return answer

# 위의 정답 코드와 왼손, 오른손 거리 계산 하는 변수 이름만 바뀌었는데 왜 이건 정답이 아닐까 ?
def solution(numbers, hand):
	for index, value in enumerate(numbers):
		if value == 0:
			numbers[index] = 11

	answer = ''
	curLeft = 10
	curRight = 12

	left = [1, 4, 7]
	center = [2, 5, 8, 11]
	right = [3, 6, 9]

	for finger in numbers:

		if finger in left:
			answer += 'L'
			curLeft = finger

		elif finger in right:
			answer += 'R'
			curRight = finger

		elif finger in center:

			checkLeft = abs(finger - curLeft)
			checkRight = abs(finger - curRight)
			print("check",checkLeft, checkRight)
			if checkLeft == 1 or checkLeft == 3:
				leftDistance = 1
			elif checkLeft == 2 or checkLeft == 4 or checkLeft == 6:
				leftDistance = 2
			elif checkLeft == 5 or checkLeft == 7 or checkLeft == 9:
				leftDistance = 3
			elif checkLeft == 8 or checkLeft == 10:
				leftDistance = 4

			if checkRight == 1 or checkRight == 3:
				rightDistance = 1
			elif checkRight == 2 or checkRight == 4 or checkRight == 6:
				rightDistance = 2
			elif checkRight == 5 or checkRight == 7 or checkRight == 9:
				rightDistance = 3
			elif checkRight == 8 or checkRight == 10:
				rightDistance = 4

			print("Distance", leftDistance, rightDistance)
			if leftDistance < rightDistance:
				answer += 'L'
				curLeft = finger
			elif leftDistance > rightDistance:
				answer += 'R'
				curRight = finger
			elif leftDistance == rightDistance:
				if hand == 'right':
					answer += 'R'
					curRight = finger
				elif hand == 'left':
					answer += 'L'
					curLeft = finger

	return answer

numbers = [2,2,1,2]
hand = 'right'

print(solution(numbers, hand))