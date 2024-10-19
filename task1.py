
def find_coins_greedy(sum, coins):
    coins.sort(reverse = True)

    result_coins = {}

    return_sum = 0
    for coin in coins:
        while (return_sum + coin <= sum):
            return_sum += coin
            if coin in result_coins:
                result_coins[coin] += 1
            else:
                result_coins[coin] = 1
            if (return_sum == sum):
                return result_coins

coins = [50, 25, 10, 5, 2, 1]
print(f"113: {find_coins_greedy(113, coins)}")
