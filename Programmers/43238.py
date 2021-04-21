def solution(n, times):
    start = 1
    end = max(times) * n
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        total_person = 0
        for time in times:
            total_person += mid // time

        if n <= total_person:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer


if __name__ == "__main__":
    n = 6
    times = [7, 10]
    print(solution(n, times))