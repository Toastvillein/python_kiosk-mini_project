hamburgers = {"1.햄버거": 2800, "2.불고기 햄버거": 3900, "3.빅햄": 4300}
drinks = {"1.콜라": 1500, "2.사이다": 1500}
sides = {"1.감자튀김": 2000, "2.치즈스틱": "2300"}
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
        input_category = int(input())
        if input_category == 1:
            print(hamburgers)
            print("원하시는 햄버거를 숫자로 입력해주세요:")
            input_hamburgers = int(input())
            if input_hamburgers < 1 or input_hamburgers > len(hamburgers):
                print(invalid_input)
                continue
            print("수량을 입력해주세요:")
            input_hamburger_quantity = int(input())
            if input_hamburger_quantity < 1:
                print(invalid_input)
                continue
            print(f"주문하신 햄버거는 {menu_list_matcher(input_hamburgers,"hamburgers")} {input_hamburger_quantity}개 입니다.")
            append_item(cart_list,menu_list_matcher(input_hamburgers,"hamburgers"),input_hamburger_quantity)


        elif input_category == 2:
            print(drinks)
            print("원하시는 음료를 숫자로 입력해주세요:")
            input_drinks = int(input())
            if input_drinks < 1 or input_drinks > len(drinks):
                print(invalid_input)
                continue
            print("수량을 입력해주세요:")
            input_drink_quantity = int(input())
            if input_drink_quantity < 1:
                print(invalid_input)
                continue
            print(f"주문하신 음료는 {menu_list_matcher(input_drinks,"drinks")} {input_drink_quantity}개 입니다.")
            append_item(cart_list,menu_list_matcher(input_drinks,"drinks"),input_drink_quantity)


        elif input_category == 3:
            print(sides)
            print("원하시는 사이드를 숫자로 입력해주세요:")
            input_sides = int(input())
            if input_sides < 1 or input_sides > len(sides):
                print(invalid_input)
                continue
            print("수량을 입력해주세요:")
            input_side_quantity = int(input())
            if input_side_quantity < 1:
                print(invalid_input)
                continue
            print(f"주문하신 사이드는 {menu_list_matcher(input_sides,"sides")} {input_side_quantity}개 입니다.")
            append_item(cart_list,menu_list_matcher(input_sides,"sides"),input_side_quantity)

        elif input_category == 4:
            break

        else:
            print(invalid_input)


def menu_list_matcher(n: int, s : str) -> str:
    if s == "hamburgers":
        for key in hamburgers:
            if key.startswith(str(n)+"."):
                result = key.split(".")[1]
                return result

    elif s == "drinks":
        for key in drinks:
            if key.startswith(str(n)+"."):
                result = key.split(".")[1]
                return result

    elif s == "sides":
        for key in sides:
            if key.startswith(str(n)+"."):
                result = key.split(".")[1]
                return result

    return "invalid menu"

def append_item(cart, item_name, quantity):
    if not cart:
        next_num = 1
    else:
        max_num = max([int(key.split(".")[0]) for key in cart.keys()])
        next_num = max_num + 1

    new_key = f"{next_num}.{item_name}"
    cart[new_key] = quantity


if __name__ == '__main__':
    category_choice()