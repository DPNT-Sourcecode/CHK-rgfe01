

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_count_map = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    sku_prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    special_offers = {'A': {3: 130, 5: 200}, 'B': {2: 45}}

    for sku in skus:
        if sku not in sku_count_map:
            print(f'{sku} is not in sku maps')
            return -1
        
        sku_count_map[sku] += 1

    print('SKU MAP IS = ', sku_count_map)
    print('SKU prices is = ', sku_prices)

    num_of_E = sku_count_map['E']
    num_of_pairs_of_E = num_of_E // 2
    sku_count_map['B'] = max(0, sku_count_map['B'] - num_of_pairs_of_E)

    print(f'New SKU Map is = ', sku_count_map)


    total_price = 0
    for sku in sku_count_map:
        # if sku == 'A':
        #     if sku_count_map[sku] % 3 == 0:
        #         sets = sku_count_map[sku] / 3
        #         total_price += sets * 130
        #         print(f'Just added {sets * 130}')

        #         continue

        # if sku == 'B':
        #     if sku_count_map[sku] % 2 == 0:
        #         sets = sku_count_map[sku] / 2
        #         total_price += sets * 45
        #         print(f'Just added {sets * 45}')
        #         continue

        while sku_count_map[sku] > 0:
            print(f'Current count is {sku_count_map[sku]}')

            if sku in special_offers:
                for offer in special_offers[sku]:
                    remainder = sku_count_map[sku] % offer
                    if remainder == 0 or remainder in special_offers[sku]:
                        offer_quantity = offer if remainder == 0 else remainder
                        print(f'Offer quanitity is {offer_quantity}')
                        num_of_orders = sku_count_map[sku] / offer_quantity
                        total_price += num_of_orders * special_offers[sku][offer_quantity]
                        sku_count_map[sku] -= num_of_orders * offer_quantity
                        print(f'Just added {num_of_orders * special_offers[sku][offer_quantity]}')

            if sku_count_map[sku] > 0:
                sku_count_map[sku] -= 1
                total_price += sku_prices[sku]
                print(f'Just added {sku_prices[sku]}')


        # total_price += sku_count_map[sku] * sku_prices[sku]
        # print(f'Just added {sku_count_map[sku] * sku_prices[sku]}')

    print(f'Total Price is = {total_price}')

    return total_price


result = checkout("AAAAAAAA")


    




