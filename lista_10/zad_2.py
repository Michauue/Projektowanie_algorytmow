import numpy as np


def knapsack(items, weight):
    n = len(items)
    cache = np.zeros((n + 1, weight + 1))

    for i in range(1, n + 1):
        for w in range(weight + 1):
            item_weight, item_value = items[i - 1]
            if item_weight > w:
                cache[i, w] = cache[i - 1, w]
            else:
                cache[i, w] = max(cache[i - 1, w], cache[i - 1, w - item_weight] + item_value)
    return cache[n, weight]

#        lampa    cormen    blender  koń        tytan    ozdoba   krzeslo  odkurzacz
items = [(2, 40), (2, 160), (3, 70), (15, 300), (1, 70), (4, 25), (5, 25), (6, 180)]

print(knapsack(items, 15))