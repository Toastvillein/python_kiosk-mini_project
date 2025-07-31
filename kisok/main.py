import menu,cart

def main():
    prompt = """
    1. 주문
    2. 장바구니
    3. 종료

    원하는 메뉴의 숫자를 입력해주세요: 
    """

    while True:
        print(prompt)
        input_number = int(input())
        if input_number == 1:
            menu.category_choice()
        elif input_number == 2:
            cart.cart_list_choice()
        elif input_number == 3:
            print("종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")
            continue

if __name__ == '__main__':
    main()