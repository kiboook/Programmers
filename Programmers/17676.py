import datetime


def solution(lines):
    answer = 0

    split_data = []
    for data in lines:
        tmp = data.split()
        complete_time = datetime.datetime.strptime(tmp[0] + ' ' + tmp[1], '%Y-%m-%d %H:%M:%S.%f')
        split_data.append([complete_time, tmp[2]])

    for idx in range(len(split_data)):
        split_data[idx][1] = round(float(split_data[idx][1][:-1]) - 0.001, 3)

        tmp = str(split_data[idx][1]).split('.')
        sec = int(tmp[0])
        millisec = int(tmp[1])

        start_time = split_data[idx][0] - datetime.timedelta(seconds=sec)
        start_time = start_time - datetime.timedelta(milliseconds=millisec)

        print(start_time)

    return answer


if __name__ == "__main__":
    lines = [
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s"
    ]

    print(solution(lines))
