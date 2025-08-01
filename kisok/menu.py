all_menus = {
    '불고기버거': 5000, '치즈버거': 4500,
    '콜라': 2000, '사이다': 2000,
    '감자튀김': 2500, '치즈스틱': 1500
}

menu_categories = {
    "hamburgers": {'1.불고기버거': 5000, '2.치즈버거': 4500},
    "drinks": {'1.콜라': 2000, '2.사이다': 2000},
    "sides": {'1.감자튀김': 2500, '2.치즈스틱': 1500}
} # 딕셔너리 내에 딕셔너리를 넣어 여러개로 나뉘어 있던 딕셔너리를 하나로 통합

invalid_input = "잘못된 입력입니다."
cart_list = {}


def category_choice():
    category_prompt = """
    1. 햄버거
    2. 음료
    3. 사이드
    4. 뒤로
    
    원하는 메뉴를 숫자로 입력해주세요:
    """

    while True:
        print(category_prompt)
        try:
            input_category = int(input())
        except ValueError:
            print(invalid_input)
            continue

        if input_category == 1:
            process_order("hamburgers") # 중복되던 프로세스를 함수로 만들어 코드 최적화
        elif input_category == 2:
            process_order("drinks")
        elif input_category == 3:
            process_order("sides")
        elif input_category == 4:
            break
        else:
            print(invalid_input)
            continue


def menu_list_matcher(category_name, item_number):
    """카테고리와 번호를 이용해 메뉴 이름을 찾아 반환합니다."""
    menu_to_search = menu_categories[category_name]
    for key in menu_to_search:
        if key.startswith(f"{item_number}."):
            return key.split('.')[1]  # '1.불고기버거' -> '불고기버거'
    return None  # 메뉴를 찾지 못한 경우

def append_item(cart, item_name, quantity):
    """
    메뉴 이름과 수량을 cart_list에 저장하고 동시에 넘버링을 통해 cart.py에서의 수정 함수에 사용이 용이하게 끔 만듬
    """
    existing_key = None # 키 초기화
    for key in cart: # cart_list를 돌면서 key의 넘버링을 떼고 비교해서 장바구니에 이미 같은 메뉴가 들어 있는지 확인
        cart_item_name = key.split('.')[1]
        if cart_item_name == item_name:
            existing_key = key
            break

    if existing_key:
        cart[existing_key] += quantity # 만약 중복 메뉴가 있으면 수량만 증가
    else:
        if not cart:
            next_num = 1 # 만약 cart_list가 비어있다면 1로 넘버링
        else:
            max_num = max([int(key.split('.')[0]) for key in cart]) # 비어있지 않다면 존재하는 키의 넘버링 중
            next_num = max_num + 1 # 가장 높은 숫자에 1을 더해서 넘버링

        new_key = f"{next_num}.{item_name}"
        cart[new_key] = quantity
        # 햄버거를 10개 시켰을 때, cart_list = {1.햄버거 : 10} 이런식으로 추가됨.


def process_order(category_name):
    """
    사용자에게 카테고리 메뉴를 보여주고, 주문을 받아 장바구니에 추가하는 전체 과정을 처리합니다.
    - category_name: "hamburgers", "drinks", "sides" 등 menu_categories의 키 이름
    """
    # 1. 해당 카테고리의 메뉴판 가져오기
    current_menu = menu_categories[category_name]
    print(current_menu)

    # 2. 사용자에게 메뉴 번호 입력받기 (오류 처리 포함)
    try:
        item_number_str = input(f"원하시는 {category_name[:-1]}를(을) 숫자로 입력해주세요: ") # hambergers가 입력되면
        item_number = int(item_number_str) # hamburger로 출력되게끔 슬라이싱

        # 메뉴판에 있는 번호인지 확인
        item_key = f"{item_number}.{menu_list_matcher(category_name, item_number)}"
        if item_key not in current_menu:
            print("메뉴에 없는 번호입니다.")
            return

    except (ValueError, TypeError): # 잘못된 입력 시에 예외처리
        print(invalid_input)
        return

    # 3. 사용자에게 수량 입력받기 (오류 처리 포함)
    try:
        quantity = int(input("수량을 입력해주세요: "))
        if quantity < 1:
            print("수량은 1 이상의 값이어야 합니다.")
            return
    except ValueError:
        print(invalid_input)
        return

    # 4. 장바구니에 추가
    item_name = menu_list_matcher(category_name, item_number)
    if item_name:
        append_item(cart_list, item_name, quantity)
        print(f"✅ [{item_name}] {quantity}개가 장바구니에 추가되었습니다.")
        print("현재 장바구니:", cart_list)
    else:
        print("메뉴를 찾지 못했습니다.")


if __name__ == '__main__':
    category_choice()