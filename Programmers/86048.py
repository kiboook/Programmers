from collections import deque


def solution(enter, leave):
    answer = {i + 1: 0 for i in range(len(enter))}

    room = []
    deque_enter = deque(enter)
    deque_leave = deque(leave)
    while deque_leave:
        # 1. 퇴실의 top이 room에 있을때 까지 입실한다.
        while deque_leave[0] not in room:
            enter_people = deque_enter.popleft()
            room.append(enter_people)

        # 2. 퇴실의 top이 room에 있다면
        # 3. 퇴실하는 사람은 len(room) - 1 명을 무조건 만난다.
        # 4. 방을 나가고 퇴실 목록에서 삭제한다.
        leave_people = deque_leave[0]
        answer[leave_people] += len(room) - 1
        room.remove(leave_people)
        deque_leave.popleft()

        # 5. 방에 있는 사람들은 무조건 방금 나간 사람을 만났기 때문에 만난 사람을 1 더해준다.
        for people in room:
            answer[people] += 1

    return list(answer.values())


if __name__ == "__main__":
    enter = [1, 4, 2, 3]
    leave = [2, 1, 3, 4]

    print(solution(enter, leave))
