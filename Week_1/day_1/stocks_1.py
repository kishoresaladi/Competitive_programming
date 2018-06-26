def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('2 values are required')

    
    min_pro  = stock_prices[0]
    max_pro = stock_prices[1] - stock_prices[0]

 
    for i in range(1, len(stock_prices)):
        current_var = stock_prices[i]

        
        overall_profit = current_var - min_pro

        
        max_pro = max(max_pro, overall_profit)

        min_pro  = min(min_pro, current_var)

    return max_pro