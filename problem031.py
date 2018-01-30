
def coinCount(target):
    """Counts how to make a target number of cents with British coins."""
    coins = [1,2,5,10,20,50,100,200]
    ways = [1] + [0]*target

    for i in range(len(coins)):
        for j in range(coins[i],target+1):
            ways[j] += ways[j - coins[i]]

    return ways[-1]

print(coinCount(200)) # 73682
