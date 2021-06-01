import numpy as np


def knapsackProblem(items, weight):
    n = len(items)
    temp = np.zeros((n + 1, weight + 1))

    for i in range(1, n + 1):
        for w in range(weight + 1):
            item_weight, item_value = items[i - 1]
            if item_weight > w:
                temp[i, w] = temp[i - 1, w]
            else:
                temp[i, w] = max(temp[i - 1, w], temp[i - 1, w - item_weight] + item_value)
    print(temp)
    return print('Programowanie dynamiczne:',temp[n, weight])

def knapsackProblemGreedy(items, weight):
    n = len(items)
    result = 0
    items = sorted(items, key=lambda item: item[1])
    for i in range(1,n+1):
        item_weight, item_value = items[-i]
        if item_weight <= weight:
            result = result + item_value
            weight = weight - item_weight
    return print('Podejście zachłanne:',result)


#    (weight, value)
items = [(2, 40),
        (2, 160),
        (3, 70),
        (8, 230),
        (1, 70),
        (4, 25),
        (5, 25),
        (6, 180)]


knapsackProblem(items, 15)
knapsackProblemGreedy(items, 15)