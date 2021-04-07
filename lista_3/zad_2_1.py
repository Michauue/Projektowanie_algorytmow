import math

def starter(p,xd):
    global tab
    tab = []
    czp(p,xd)
    return tab


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


def xd(p):
    xd = int(math.floor(math.sqrt(p)))
    return xd


def pczp(a):
    xd_a = xd(a)
    tab_a = czp(a,xd_a)
    return tab_a

def aczp(a,b):
    xd_a = xd(a)
    xd_b = xd(b)
    tab_a = starter(a,xd_a)
    tab_b = starter(b,xd_b)
    len_a = len(tab_a)
    len_b = len(tab_b)
    temp_tab = []
    for i in range(0,len_a):
        for j in range(0,len_b):
            if tab_a[i] == tab_b[j]:
                temp_tab.append(tab_b[j])
                tab_b.remove(tab_b[j])
                len_b -= 1
                break
    if not temp_tab:
            print("Brak wspólnych czynników pierwszych")
    result = 1
    for i in range(0,len(temp_tab)):
        result = result * temp_tab[i]
        
    return result


def aeuc(x, y):
    if y == 0:
        return x
    else:
        return aeuc(y, x % y)


a = 1584
b = 5
print("NWD aeuc liczb", a, "i", b, "to:",aeuc(a,b))
print("NWD aczp liczb", a, "i", b, "to:",aczp(a,b))