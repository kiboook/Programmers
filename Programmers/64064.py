from itertools import permutations


def make_ban_list(user_id, banned_id):
    # 제재 아이디 별 제재 가능한 유저 아이디 리스트
    ban_id_list = []
    for ban in banned_id:
        # 제재 가능한 유저 아이디를 담을 리스트
        ban_list = []
        # 제재 아이디로 제재가 가능한 아이디인지 검사한다
        for user in user_id:
            if len(ban) == len(user):
                isBanned = True
                for i, j in zip(user, ban):
                    # 제재할 수 없는 아이디라면 멈춘다
                    if j != '*' and i != j:
                        isBanned = False
                        break
                # 제재할 수 있는 아이디라면 추가한다
                if isBanned:
                    ban_list.append(user)
        ban_id_list.append(ban_list)

    return ban_id_list


def solution(user_id, banned_id):
    # 1. 제재 아이디 별 제재가 가능한 유저 아이디 목록을 구한다
    ban_id_list = make_ban_list(user_id, banned_id)

    answer = []
    # 2. 제재 아이디 별 제재를 할 유저 아이디 순열을 구한다
    for users in permutations(user_id, len(banned_id)):
        flag = True
        for user, ban_list in zip(users, ban_id_list):
            # 3. 제재 아이디가 제재를 할 수 없는 유저 아이디라면 멈춘다
            if user not in ban_list:
                flag = False
                break
        # 4. 모두 제재를 할 수 있는 유저라면 중복 방지를 위해 집합으로 바꾼 뒤 정답에 추가한다
        users = set(users)
        if flag and users not in answer:
            answer.append(users)

    return len(answer)


if __name__ == "__main__":
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "*rodo", "******", "******"]
    print(solution(user_id, banned_id))
