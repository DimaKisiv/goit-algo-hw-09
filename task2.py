def find_min_coins(amount_left, coins, memo=None):
    if memo is None:
        memo = {}

    if amount_left == 0:
        return {}  
    if amount_left < 0:
        return None  

    if amount_left in memo:
        return memo[amount_left]

    best_combination = None

    for coin in coins:
        new_amount = amount_left - coin
        new_combination = find_min_coins(new_amount, coins, memo)

        if new_combination is not None:  
            new_combination = new_combination.copy()
            if coin in new_combination:
                new_combination[coin] += 1
            else:
                new_combination[coin] = 1

            if best_combination is None or sum(new_combination.values()) < sum(best_combination.values()):
                best_combination = new_combination

    memo[amount_left] = best_combination
    return dict(sorted(best_combination.items()))

coins = [50, 25, 10, 5, 2, 1]
print(f"143: {find_min_coins(143, coins)}")
print(f"113: {find_min_coins(113, coins)}")
