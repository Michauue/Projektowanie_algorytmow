import math

def sera(p):
    tab = [0] * (p+1)
    final_tab = []
    z = int(math.floor(math.sqrt(p)))+1
    for i in range(2,z):
        if tab[i] == 0:
            final_tab.append(i)
            tab[i] = 1
            for j in range(i,len(tab)):
                t = i*j
                if t > p:
                    break
                tab[t] = 1;
    for i in range(2,len(tab)):
        if tab[i] == 0:
            final_tab.append(i)
    return final_tab

p = 213
print("Wszytkie liczby pierwsze z zakresu od <2,p> to:",sera(p))