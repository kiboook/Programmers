def solution(n, stations, w):
    answer = 0
    idx = 1
    len_stations = len(stations)
    station_idx = 0
    while idx <= n:
        if station_idx < len_stations and stations[station_idx] - w <= idx <= stations[station_idx] + w:
            idx = stations[station_idx] + w + 1
            station_idx += 1
        else:
            answer += 1
            idx += w * 2 + 1

    return answer


if __name__ == "__main__":
    N = 16
    stations = [9]
    W = 2

    print(solution(N, stations, W))