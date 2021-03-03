shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    discounted_price_sum = 0
    for i in range(len(prices)):
        if i < len(coupons):
            discounted_price = ((100 - coupons[i]) * 0.01) * prices[i]
            discounted_price_sum += discounted_price
        else:
            discounted_price_sum += prices[i]

    return int(discounted_price_sum)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
