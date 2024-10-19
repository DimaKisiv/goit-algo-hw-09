
coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(sum):
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

print(find_coins_greedy(143))
print(find_coins_greedy(113))
