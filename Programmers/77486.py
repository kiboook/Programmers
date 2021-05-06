def solution(enroll, referral, seller, amount):
    answer = {name: 0 for name in enroll}

    # 1. 부모 정보를 저장한 사전 생성한다.
    parent_info = {name: "" for name in enroll}
    for parent, child in zip(referral, enroll):
        if parent != '-':
            parent_info[child] = parent

    # 2. 판매 정보를 저장한 리스트 생성, 같은 이름이 있을 수 있기 때문에 리스트로 생성한다.
    seller_info = [[name, cost * 100] for name, cost in zip(seller, amount)]
    
    # 3. 루트까지 올라가며 판매금액의 10% 정산한다.
    for info in seller_info:
        me = info[0]
        parent = parent_info[me]

        start_money = info[1]
        # 4. 수익금에 대한 10퍼센트를 계산한다.
        parent_cost = int(start_money * 0.1)
        # 5. 절삭이 있기 때문에 0.9를 곱해서 계산하면 안되고 상납할 돈에서 빼야한다.
        my_cost = start_money - parent_cost
        answer[me] += my_cost

        # 6. 재귀나 반복문을 통해 부모노드를 계속 탐색한다.
        while parent != "":
            start_money = parent_cost
            parent_cost = int(start_money * 0.1)
            my_cost = start_money - parent_cost

            me = parent
            parent = parent_info[me]
            answer[me] += my_cost

    return list(answer.values())


if __name__ == "__main__":
    enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    seller = ["young", "john", "tod", "emily", "mary"]
    amount = [12, 4, 2, 5, 10]

    print(solution(enroll, referral, seller, amount))
