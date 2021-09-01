def solution(scores):
    answer = ''

    # 계산하기 편하게 배열 회전
    for idx, spin in enumerate(zip(*scores)):
        scores[idx] = list(spin)

    for idx, score in enumerate(scores):
        max_score = max(score)
        max_count = score.count(max_score)

        min_score = min(score)
        min_count = score.count(min_score)

        # 최고점수가 자신이 유일한 경우 이 점수는 제외한다.
        if max_score == score[idx] and max_count == 1:
            score.remove(max_score)
        # 최저점수가 자신이 유일한 경우 이 점수는 제외한다.
        elif min_score == score[idx] and min_count == 1:
            score.remove(min_score)

        avg = sum(score) / len(score)
        if avg >= 90:
            answer += 'A'
        elif avg >= 80:
            answer += 'B'
        elif avg >= 70:
            answer += 'C'
        elif avg >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer


if __name__ == "__main__":
    scores = [[100, 90, 98, 88, 65],
              [50, 45, 99, 85, 77],
              [47, 88, 95, 80, 67],
              [61, 57, 100, 80, 65],
              [24, 90, 94, 75, 65]]

    print(solution(scores))