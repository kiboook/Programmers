def solution(s):
    result = ""
    idx = 0
    while idx < len(s):
        if '0' <= s[idx] <= '9':
            result += s[idx]
            idx += 1
            continue

        if s[idx] == 'z':
            result += '0'
            idx += 4
        elif s[idx] == 'o':
            result += '1'
            idx += 3
        elif s[idx] == 't':
            if s[idx + 1] == 'w':
                result += '2'
                idx += 3
            elif s[idx + 1] == 'h':
                result += '3'
                idx += 5
        elif s[idx] == 'f':
            if s[idx + 1] == 'o':
                result += '4'
            elif s[idx + 1] == 'i':
                result += '5'
            idx += 4
        elif s[idx] == 's':
            if s[idx + 1] == 'i':
                result += '6'
                idx += 3
            elif s[idx + 1] == 'e':
                result += '7'
                idx += 5
        elif s[idx] == 'e':
            result += '8'
            idx += 5
        elif s[idx] == 'n':
            result += '9'
            idx += 4

    return int(result)


def solution2(s):
    info_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    result = s
    for key, value in info_dict.items():
        result = result.replace(key, value)
    return result


if __name__ == "__main__":
    s = "one4seveneight"
    print(solution2(s))