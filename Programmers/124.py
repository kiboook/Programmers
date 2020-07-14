def solution(n):
    answer = ''
    while n > 0:
        n, mod = divmod(n, 3)
        if mod != 0:
            answer += str(mod)
        else:
            answer += '4'
            n -= 1

    return answer[::-1]


n = 28
print(solution(n))