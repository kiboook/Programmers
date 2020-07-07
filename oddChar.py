def solution(string):
    answer = ''
    idx = 0
    for val in string:
        if val == ' ':
            idx = 0
            answer += val
            continue

        if idx % 2 == 0:
            answer += val.upper()
        elif idx % 2 != 0:
            answer += val.lower()
        idx += 1

    return answer

s = 'try hello world'
print(solution(s))
