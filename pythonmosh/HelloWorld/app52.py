def calc_cost(truck_price = int(input("Your truck price in numbers: ")), shipping_price = int(input("Your shipping price in numbers: "))
):
    total_price = truck_price + shipping_price - (15 / 100 * truck_price)
    print(f"Your total cost is {total_price}")


calc_cost()
