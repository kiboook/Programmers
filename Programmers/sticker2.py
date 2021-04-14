def solution(sticker):
    N = len(sticker)
    if N == 1:
        return max(sticker)

    dp1 = [0 for _ in range(N)]
    dp1[0] = dp1[1] = sticker[0]
    for i in range(2, N - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    dp2 = [0 for _ in range(N)]
    dp2[1] = sticker[1]
    for i in range(2, N):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    return max(max(dp1), max(dp2))


if __name__ == "__main__":
    sticker = [14, 6, 5, 11, 3, 9, 2, 10]
    print(solution(sticker))