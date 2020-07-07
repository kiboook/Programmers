def solution(priorities, location):
    find_loc = [i for i in range(len(priorities))]
    print_cnt = 0

    while(True):
        if priorities[0] != max(priorities):  # 나보다 우선순위 높은게 있다 ?
            item = priorities.pop(0)
            priorities.append(item)

            item = find_loc.pop(0)
            find_loc.append(item)
        else:  # 내가 우선순위가 제일 높다 ?
            priorities.pop(0)
            print_cnt += 1

            if find_loc.pop(0) == location:
                return print_cnt


priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))

