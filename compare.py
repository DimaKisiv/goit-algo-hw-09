import timeit
from task1 import find_coins_greedy
from task2 import find_min_coins, find_min_coins_recursive, find_min_coins_bottom_up

coins = [1, 2, 5, 10, 25, 50]
amounts = [113, 534, 19234, 192346]

for amount in amounts:
    time_greedy = timeit.timeit(lambda: find_coins_greedy(amount, coins), number=10)
    time_dyhamic = timeit.timeit(lambda: find_min_coins(amount, coins), number=10)
    try:
        time_dynamic_recursive = timeit.timeit(lambda: find_min_coins_recursive(amount, coins), number=10)
    except Exception as err:
        time_dynamic_recursive = err
    time_dynamic_bottom_up = timeit.timeit(lambda: find_min_coins_bottom_up(amount, coins), number=10)

    print(f"{amount} greedy: {time_greedy:5f}")
    print(f"{amount} dyhamic iterative: {time_dyhamic:5f}")
    if (isinstance(time_dynamic_recursive, (int, float))):
        print(f"{amount} dynamic recursive: {time_dynamic_recursive:5f}")
    else:
        print(f"{amount} dynamic recursive: {time_dynamic_recursive}")
    print(f"{amount} dynamic bottom up: {time_dynamic_bottom_up:5f}")