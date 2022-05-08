shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    if len(prices)>len(coupons):
        for i in range(len(prices)-len(coupons)):
            coupons.append(0)
    elif len(prices)<len(coupons):
        coupons=coupons[:-(len(coupons)-len(prices))]
    i=0
    sum=0
    for items in prices:
        sum+=items*((100-coupons[i])/100)
        i+=1
    return sum


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))