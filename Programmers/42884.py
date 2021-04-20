def solution(routes):
    routes.sort(key=lambda x: x[1])
    answer = 1
    CCTV = routes[0][1]

    for route in routes[1:]:
        if CCTV < route[0]:
            answer += 1
            CCTV = route[1]

    return answer


if __name__ == "__main__":
    routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
    print(solution(routes))
