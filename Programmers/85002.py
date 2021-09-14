def solution(weights, head2head):
    answer_info = list()
    total_game = len(head2head) - 1

    for my_num in range(total_game + 1):
        win_count = 0
        lose_count = 0
        heavy_win_count = 0
        person_info = []

        for enemy_num in range(total_game + 1):
            if my_num != enemy_num:
                if head2head[my_num][enemy_num] == 'W':
                    win_count += 1
                    if weights[my_num] < weights[enemy_num]:
                        heavy_win_count += 1
                if head2head[my_num][enemy_num] == 'L':
                    lose_count += 1

        if win_count != 0 or lose_count != 0:
            person_info.append(win_count / (win_count + lose_count) * 100)
        else:
            person_info.append(0)
        person_info.append(heavy_win_count)
        person_info.append(weights[my_num])
        person_info.append(my_num + 1)
        answer_info.append(person_info)

    answer = list()
    for info in sorted(answer_info, key=lambda x: (x[0], x[1], x[2], -x[3]), reverse=True):
        answer.append(info[3])

    return answer


if __name__ == "__main__":
    weights = [50, 82, 75, 120]
    head2head = ["NLWL", "WNLL", "LWNW", "WWLN"]

    print(solution(weights, head2head))