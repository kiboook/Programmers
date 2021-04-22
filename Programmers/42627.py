import heapq
from collections import deque


def solution(jobs):
    # 1. 가장 먼저 할 작업 선정
    jobs.sort(key=lambda x: (x[0], x[1]))
    # 2. 먼저 수행 할 작업을 왼쪽에 넣고 뺄 것이기 때문에 deque 선언
    jobs = deque(jobs)
    # 3. 평균 작업 시간을 계산하기 위한 전체 작업 시간과 작업 개수
    total_time = 0
    n = len(jobs)
    # 4. 맨 처음 작업 종료 시간
    time = jobs[0][0]
    # 5. 작업 시간이 가장 큰 작업 정렬 용 힙 선언
    heap = []

    while jobs:
        # 6. 수행 할 작업 선정
        request, work = jobs.popleft()
        # 7. 작업 종료 후 시간
        time += work
        # 8. 작업 종료 후 시간에서 기다린 시간을 빼 전체 소요시간을 구한다
        total_time += time - request

        # 9. 작업이 끝나기 전에 요청 된 새로운 작업들 가져오기
        while jobs and jobs[0][0] < time:
            request, work = jobs.popleft()
            # 10. 최대힙으로 해야 나중에 작업 시간이 작은 순으로 넣어 줄 수 있다
            heapq.heappush(heap, (-work, request))

        # 11. 가져온 작업들 중 작업 시간이 가장 큰 순서로 넣어주기
        while heap:
            work, request = heapq.heappop(heap)
            jobs.appendleft((request, -work))

    return total_time // n


if __name__ == "__main__":
    jobs = [[0, 10], [4, 10], [15, 2], [5, 11]]
    print(solution(jobs))