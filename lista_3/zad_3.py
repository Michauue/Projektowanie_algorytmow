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


p = 22469
print(fermat_test(p))