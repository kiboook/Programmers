def solution(table, languages, preferences):
    answer = ""

    language_score = dict()
    for data in table:
        tmp = data.split()
        language_score[tmp[0]] = list(reversed(tmp[1:]))

    max_score = 0
    for job in language_score:
        cur_score = 0
        for idx, job_language in enumerate(language_score[job]):
            for user_language, score in zip(languages, preferences):
                if job_language == user_language:
                    cur_score += score * (idx + 1)

        if max_score < cur_score:
            max_score = cur_score
            answer = job
        elif max_score == cur_score:
            answer = sorted([answer, job])[0]

    return answer


if __name__ == "__main__":
    table = ["SI JAVA JAVASCRIPT SQL PYTHON C#",
             "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
             "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
             "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
             "GAME C++ C# JAVASCRIPT C JAVA"]
    languages = ["JAVA", "JAVASCRIPT"]
    preferences = [7, 5]

    print(solution(table, languages, preferences))