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
    # for i in tab_a:
    #     for j in tab_b:
    #         if tab_a[i-1] == tab_b[j-1]:
    #             print("git")
    return tab_a, tab_b


def aeuc(a,b):
    r = 1
    if a == b or b == 0:
        return a
    elif a < b:
        temp = a
        a = b
        b = temp
    while r !=0:
         r = a % b
         a = b
         b = r
         if r != 0:
            last_r = r
    return last_r


a = 1560
b = 124
# print("NWD aeuc liczb", a, "i", b, "to:",aeuc(a,b))
print("NWD aczp liczb", a, "i", b, "to:",aczp(a,b))