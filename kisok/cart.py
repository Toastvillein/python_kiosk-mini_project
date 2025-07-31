from menu import cart_list,hamburgers,drinks,sides

def cart_list_choice():
    cart_prompt = """
    1. 장바구니 수정
    2. 결제
    3. 뒤로
    """
    while True:
        print(cart_prompt)
        input_cart_choice = int(input())
        if input_cart_choice == 1:
            print(cart_list)
            print("수정하고 싶은 메뉴를 숫자로 입력해주세요:")
            input_modifying = int(input())
            if input_modifying < 1 or input_modifying > len(cart_list):
                print("잘못된 입력입니다.")
                continue
            print("수정하고 싶은 갯수를 숫자로 입력해주세요:")
            input_quantity = int(input())
            if input_quantity < 0 :
                print("잘못된 입력입니다.")
                continue
            cart_quantity_modifier(input_modifying, input_quantity)

        elif input_cart_choice == 2:
            print(cart_list)
            print(f"장바구니에 담긴 모든 상품의 가격은 {cart_payment_calculator()}원 입니다.")
            print("결제하시겠습니까? [yes/no]")
            input_yes_or_no = str(input())
            if input_yes_or_no == "yes":
                print("결제되었습니다.")
                cart_list.clear()
                break
            elif input_yes_or_no == "no":
                continue
            else:
                print("잘못된 입력입니다.")
                continue

        elif input_cart_choice == 3:
            break

        else:
            "잘못된 입력입니다."
            continue

def cart_quantity_modifier(input_modifying,input_quantity):
    """input_modifying 값을 가진 키의 갯수(value)를 input_quantity개로 수정하는 함수"""
    # 💥 원본 딕셔너리 대신, 키 목록의 '복사본'을 만들어 반복합니다. 딕셔너리를 list() 형태로 감싸면 키 목록을 지닌 리스트가 된다.
    for key in list(cart_list):
        if key.startswith(str(input_modifying)) and input_quantity == 0:
            del cart_list[key]
        elif key.startswith(str(input_modifying)):
            cart_list[key] = input_quantity

    print("수정되었습니다.")
    print(cart_list)

def cart_payment_calculator():
    result = 0
    # cart_list 가공
    processed_carts = {}
    for key,value in cart_list.items():
        name = key.split('.')[1]
        processed_carts[name] = value

    processed_hamburgers = {}
    for key,value in hamburgers.items():
        name = key.split('.')[1]
        processed_hamburgers[name] = value

    processed_drinks = {}
    for key,value in drinks.items():
        name = key.split('.')[1]
        processed_drinks[name] = value

    processed_sides = {}
    for key,value in sides.items():
        name = key.split('.')[1]
        processed_sides[name] = value

    for name in processed_carts:
        if name in processed_hamburgers:
            result += processed_carts[name] * processed_hamburgers[name]

    for name in processed_carts:
        if name in processed_drinks:
            result += processed_carts[name] * processed_drinks[name]

    for name in processed_carts:
        if name in processed_sides:
            result += processed_carts[name] * processed_sides[name]

    return result
