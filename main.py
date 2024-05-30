import datetime  # 날짜와 시간을 다루기 위한 datetime 모듈을 임포트
balance = 0.0  # 초기 잔액 설정

b_is_exit = 0

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":

        try:
            amount = float(input("금액 입력 (수입은 양수, 지출은 음수로 입력): "))#수입,지출이랑 어디서 뭐하다 돈을 썻는지 적기위한 코드들
            category = input("카테고리 입력 (예: '식비', '월급'): ")
            description = input("설명 입력: ")
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 현재 날짜와 시간을 문자열로 포맷
            entry = {
                'date': date,
                'amount': amount,
                'category': category,
                'description': description,
                'balance': balance + amount  # 거래 후 잔액 계산
            }
            
            balance += amount  # 잔액 업데이트
            
        
        break

    elif func == "2":

        break

    elif func == "3":

        break

    elif func == "?":
        print("도움말 입력.")

        break

    else:
        b_is_exit = not b_is_exit

