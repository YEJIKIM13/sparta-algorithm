shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

# 가장 비싼 것 가장 많이 할인 받는 방법
# sort 함수를 쓸 자격이 주어졌다!
# 비싼 가격을 높은 할인률로 할인받고 싶다


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)  # 내림차순 정
    coupons.sort(reverse=True)  # 내림차순 정렬
    # 쿠폰 수와 가격 개수가 다를 수 있기 때문에 while 문과 index 를 활용해서 사용해보도록 하자! 렬

    price_index = 0
    coupon_index = 0
    max_discounted_price = 0  # 최대 할인 가격

    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index]) / 100
        price_index += 1
        coupon_index += 1

    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1
    return max_discounted_price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
