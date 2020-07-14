def solution(board, moves):
    answer = 0
    basket = [0]

    for i in moves:
    	for j in range(len(board[0])):
    		if board[j][i-1] != 0:
    			basket.append(board[j][i-1])
    			board[j][i-1] = 0

    			if basket[-1] == basket[-2]:
    				basket.pop()
    				basket.pop()
    				answer += 2
    			break
    			
    return answer



board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))