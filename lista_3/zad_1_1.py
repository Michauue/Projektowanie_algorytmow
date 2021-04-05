import math

def czp(p, xd):
    if p < 2:
        return tab
    tab.append(p)
    for i in range(2,xd+1):
        if p % i == 0:
            tab.pop()
            tab.append(i)
            czp(int(p/i), xd)
            break
    return tab


tab = []                                
p = 213213                              # zadana liczba p
xd = int(math.floor(math.sqrt(p)))      # pierwiastek z n
print("Czynniki pierwsze liczby", p, "to:",czp(p, xd))