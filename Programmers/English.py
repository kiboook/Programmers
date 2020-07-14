# 영어 끝말잇기 문제

def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1] or words[i] in words[:i]:
            return [i % n + 1, i // n + 1]
    else:
        return [0, 0]


# n = 3
# words = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']

n = 2
words = ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']

print(solution(n, words))
