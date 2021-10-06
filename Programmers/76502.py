def is_correct_bracket(s):
    open_bracket = list()
    for item in s:
        if item in ("(", "{", "["):
            open_bracket.append(item)
        else:
            if open_bracket:
                check_bracket = open_bracket.pop()
            else:
                return False

            if check_bracket == '[' and item != ']':
                return False
            if check_bracket == '(' and item != ')':
                return False
            if check_bracket == '{' and item != '}':
                return False

    if open_bracket:
        return False
    else:
        return True


def solution(s):
    answer = 0
    for i in range(len(s)):
        lotate_s = s[i:] + s[:i]
        if is_correct_bracket(lotate_s):
            answer += 1

    return answer


if __name__ == "__main__":
    s = "}]()[{"

    print(solution(s))