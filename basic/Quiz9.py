# Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#         출력 메세지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#         출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

class SoldOutEror(Exception):
    pass

try:
    chicken = 10
    waiting = 1
    while(True):
        # 치킨이 모두 소진되었을 경우 에러 발생시키고 반복문을 나간다
        if chicken == 0:
            raise SoldOutEror
            break

        print(f"[남은 치킨 : {chicken}")
        order = int(input("치킨 몇마리 주문하시겠습니까?"))

        # 주문이 1보다 작을 경우 에러 발생
        if order < 1:
            raise ValueError

        if order > chicken:
            print("재료가 부족합니다.")
        else:
            print(f"[대기번호 {waiting}] {order} 마리 주문이 완료되었습니다.")
            waiting += 1
            chicken -= order
except ValueError:
    print("잘못된 값을 입력하엿습니다.")
except SoldOutEror:
    print("재고가 소진되어 더 이상 주문을 받지 않습니다.")