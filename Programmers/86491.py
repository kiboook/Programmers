def solution(sizes):
    for index in range(len(sizes)):
        if sizes[index][0] < sizes[index][1]:
            sizes[index][0], sizes[index][1] = sizes[index][1], sizes[index][0]

    wallet = list()
    for lotate in zip(*sizes):
        wallet.append(max(lotate))

    return wallet[0] * wallet[1]


if __name__ == "__main__":
    sizes = [[14, 4],
             [19, 6],
             [6, 16],
             [18, 7],
             [7, 11]]

    print(solution(sizes))