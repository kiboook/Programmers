# def solution(A, B):
#     answer = 0

#     A.sort()
#     B.sort()

#     for i in range(0,len(A)):
#     	for j in range(0,len(B)):
#     		if A[i] < B[j]:
#     			B.pop(j)
#     			answer += 1
#     			break


#     return answer

def solution(A, B):
    answer = 0

    A.sort()
    B.sort()

    for i in A:
    	for j in B:
    		if i < j:
    			B.remove(j)
    			answer += 1
    			break


    return answer


A = [5,1,3,7]
B = [2,2,6,8]

print(solution(A,B))

