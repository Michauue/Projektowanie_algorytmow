def fun1(n):
    if n == 0:
        return 0
    return (pow(3, n) + fun1(n - 1))


def fun2(n):
    if n == 0:
        return 0
    if n == -1:
        return 0
    return (n + fun2(n - 2))


def fun3(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (fun3(n - 1) + fun3(n - 2))


N = 30

firstTrue = True
secondTrue = True
thirdTrue = True
for i in range(0, N):
    try:
        if (pow(3, i + 1) + pow(3, i) + fun1(i - 1)) != fun1(i + 1):
            thirdTrue = False
    except RecursionError:
        pass

    try:
        if (1 + fun2(i) + fun2(i - 1) - fun2(i - 2)) != fun2(i + 1):
            thirdTrue = False
    except RecursionError:
        pass

    try:
        if (2 * fun3(i - 1) + fun3(i - 2)) != fun3(i + 1):
            thirdTrue = False
    except RecursionError:
        pass

print(f'firstTrue: {firstTrue}')
print(f'secondTrue: {secondTrue}')
print(f'thirdTrue: {thirdTrue}')
