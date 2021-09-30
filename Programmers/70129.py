def remove_zero(s):
    return "".join(s.split('0'))


def change_binary(length):
    output = []
    while length:
        output.append(str(length % 2))
        length //= 2

    return "".join(reversed(output))


def solution(s):
    work_cnt = 0
    zero_cnt = 0

    while s != '1':
        work_cnt += 1
        s_len = len(s)
        s = remove_zero(s)
        zero_cnt += s_len - len(s)
        s = change_binary(len(s))

    return [work_cnt, zero_cnt]


if __name__ == "__main__":
    s = "110010101001"
    remove_zero(s)
    print(solution(s))