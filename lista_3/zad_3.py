import random


def fermat_test(p):
    t_count = 1000
    counter = 0
    for i in range(0,t_count):
        q = random.randint(2,p-1)
        test = pow(q, p-1) % p
        if test == 1:
            counter +=1
    ratio = counter/t_count
    if ratio > 0.95:
        return "Liczba pierwsza"
    else:
        return "Liczba nie pierwsza"


def miller_rabin(p):
    if p == 2 or p == 3:
        return "Liczba pierwsza"
    if p % 2 == 0:
        return "Liczba nie pierwsza"

    r, s = 0, p - 1
    t_count = 1000

    while s % 2 == 0:
        r += 1
        s //= 2
    for z in range(t_count):
        a = random.randrange(2, p - 1)
        x = pow(a, s, p)
        if x == 1 or x == p - 1:
            continue
        for z in range(r - 1):
            x = pow(x, 2, p)
            if x == p - 1:
                break
        else:
            return "Liczba nie pierwsza"
    return "Liczba pierwsza"


p = 15645
print(fermat_test(p))
print(miller_rabin(p))
