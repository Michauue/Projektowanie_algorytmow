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
        return "Liczba pierwsza", ratio
    else:
        return "Liczba nie pierwsza", ratio

def miller_rabin_test(p):
    t_count = 100
    d = p-1
    s = 0
    while d % 2 == 0:
        s = s + 1
        d = d / 2
    for i in range(0,t_count):
        a = random.randint(2,p-2)
        x = pow(a,d) % p
        if x == 1 or x == p - 1:
            break
        j = 1
        while j < s and x != p - 1:
            x = pow(x,2) % p
            if x == 1:
                return "NIE"
            j = j + 1
            if x != p - 1:
                return "NIE"
    return "TAK"


p = 151
# print(fermat_test(p))
print(miller_rabin_test(p))