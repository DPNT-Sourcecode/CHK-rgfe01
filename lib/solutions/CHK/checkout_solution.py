

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_count_map = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    sku_prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    special_offers = {'A': [3, 130], 'B': [2, 45]}

    for sku in skus:
        if sku not in sku_count_map:
            return -1
        
        sku_count_map[sku] += 1

    total_price = 0
    for sku in sku_count_map:

        while sku_count_map[sku] > 0:

            if sku in special_offers:
                if sku_count_map[sku] % special_offers[sku][0] == 0:
                    num_of_orders = sku_count_map[sku] / special_offers[sku][0]
                    total_price += num_of_orders * special_offers[sku][1]
                    sku_count_map[sku] -= num_of_orders * special_offers[sku][0]

            if sku_count_map[sku] > 0:
                sku_count_map[sku] -= 1
                total_price += sku_prices[sku]

    return total_price





    
