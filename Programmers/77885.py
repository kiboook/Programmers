def find_answer(number):
    bin_num = bin(number)[2:].zfill(18)
    if number % 2 == 0:
        return number + 1
    else:
        zero_idx = bin_num.rfind('0')
        list_bin_num = list(bin_num)
        list_bin_num[zero_idx] = '1'
        list_bin_num[zero_idx + 1] = '0'
        return int(''.join(list_bin_num), 2)


def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(find_answer(num))

    return answer


if __name__ == "__main__":
    numbers = [2, 7]

    print(solution(numbers))