

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_count_map = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    sku_prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

    for sku in skus:
        if sku not in sku_count_map:
            print(f'{sku} is not in sku maps')
            return -1
        
        sku_count_map[sku] += 1

    print('SKU MAP IS = ', sku_count_map)
    print('SKU prices is = ', sku_prices)

    total_price = 0
    for sku in skus:
        if sku == 'A':
            if sku_count_map[sku] % 3 == 0:
                sets = sku_count_map[sku] / 3
                total_price += sets * 130
                continue

        if sku == 'B':
            if sku_count_map[sku] % 2 == 0:
                sets = sku_count_map[sku] / 2
                total_price += sets * 45
                continue

            total_price += sku_count_map[sku] * sku_prices[sku]

    print(f'Total Prices are = {total_price}')

    return total_price


result = checkout("ABC")


    




