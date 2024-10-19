def find_min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  
    
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    if dp[amount] == float('inf'):
        return None

    result_coins = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result_coins:
            result_coins[coin] += 1
        else:
            result_coins[coin] = 1
        current_amount -= coin

    return result_coins


def find_min_coins_recursive(amount_left, coins, memo=None):
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
        new_combination = find_min_coins_recursive(new_amount, coins, memo)

        if new_combination is not None: 
            potential_solution = new_combination.copy()

            if coin in potential_solution:
                potential_solution[coin] += 1
            else:
                potential_solution[coin] = 1

            if best_combination is None or sum(potential_solution.values()) < sum(best_combination.values()):
                best_combination = potential_solution

    memo[amount_left] = best_combination
    return dict(sorted(best_combination.items()))

def find_min_coins_bottom_up(target_amount, coin_denominations):
    dp = [float('inf')] * (target_amount + 1)
    dp[0] = 0  

    coin_used = [None] * (target_amount + 1)

    for amount in range(1, target_amount + 1):
        for coin in coin_denominations:
            if coin <= amount:
                if dp[amount - coin] + 1 < dp[amount]:
                    dp[amount] = dp[amount - coin] + 1
                    coin_used[amount] = coin

    if dp[target_amount] == float('inf'):
        return None

    result_coins = {}
    current_amount = target_amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result_coins:
            result_coins[coin] += 1
        else:
            result_coins[coin] = 1
        current_amount -= coin

    return result_coins


coins = [50, 25, 10, 5, 2, 1]
print(f"113 dynamic: {find_min_coins(113, coins)}")
print(f"113 recursive: {find_min_coins_recursive(113, coins)}")
print(f"113 bottom_up: {find_min_coins_bottom_up(113, coins)}")
