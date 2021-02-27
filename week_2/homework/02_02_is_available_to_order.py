shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


# 집합 자료형 이용해서 해결!
# 존재 여부 쉽게 확인 가능
def is_available_to_order(menus, orders):
    menus_set = set(menus)  # O(n)
    for order in orders:  # m -> O(m)
        if order not in menus_set:  # O(1)
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)
