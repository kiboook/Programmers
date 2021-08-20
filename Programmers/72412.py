import bisect


def solution(info, query):
    answer = []
    query_dict = dict()

    # 1. 가능한 모든 쿼리문 생성
    for a in ['java', 'python', 'cpp', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['pizza', 'chicken', '-']:
                    query_dict.setdefault((a, b, c, d), [])

    for data in info:
        split_data = data.split()
        user_info = split_data[:-1]
        user_score = int(split_data[-1])

        # 2. 조건을 충족하는 쿼리문에 점수 추가
        for a in [user_info[0], '-']:
            for b in [user_info[1], '-']:
                for c in [user_info[2], '-']:
                    for d in [user_info[3], '-']:
                        query_dict[a, b, c, d].append(user_score)

    for value in query_dict.values():
        value.sort()

    # 3. 쿼리문을 통해 특정 점수 이상의 사람 찾기
    for data in query:
        split_data = data.split()
        split_query = (split_data[0], split_data[2], split_data[4], split_data[6])
        query_score = int(split_data[7])

        size = len(query_dict[split_query])
        answer.append(size - bisect.bisect_left(query_dict[split_query], query_score))

    return answer


if __name__ == "__main__":
    info = ["java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50"]

    query = ["java and backend and junior and pizza 100",
             "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250",
             "- and backend and senior and - 150",
             "- and - and - and chicken 100",
             "- and - and - and - 150"]

    print(solution(info, query))