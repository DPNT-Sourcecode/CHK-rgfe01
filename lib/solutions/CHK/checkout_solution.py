

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_count_map = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    sku_prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

    for sku in skus:
        if sku not in sku_count_map:
            return -1
        
        sku_count_map[sku] += 1

    total_price = 0
    for sku in sku_count_map:
        if sku == 'A':
            if sku_count_map[sku] % 3 == 0:
                sets = sku_count_map[sku] / 3
                total_price += sets * 130

        elif sku == 'B':
            if sku_count_map[sku] % 2 == 0:
                sets = sku_count_map[sku] / 2
                total_price += sets * 45

        else:
            total_price += sku_count_map[sku] * sku_prices[sku]

    return total_price


    


