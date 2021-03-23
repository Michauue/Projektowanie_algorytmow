from math import sqrt

def fun1(n):
    if n == 0:
        return 0
    else:
        equation = pow(3,n)+fun1(n-1)

    return int(equation)


def fun1_2(n):                                      #analitycznie funkcja pierwsza
    equation = ((pow(3,n+1)-1)/(3-1))-1

    return int(equation)


def fun2(n):
    if n == -1 or n == 0:
        return 0
    else:
        equation = n+fun2(n-2)

    return int(equation)


def fun2_2(n):                                         #analitycznie druga funkcja
    if n % 2 == 0:
        equation = (1/2)*n*(1/2)*(n+2)
    else:
        equation = (1/4)*pow(n+1,2)

    return int(equation)


def fun3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        equation = fun3(n - 1)+fun3(n-2)

    return int(equation)


def fun3_2(n):                                                                              #analitycznie trzecia funkcja
    equation = (1/sqrt(5))*pow(((1+sqrt(5))/(2)),n) - (1/sqrt(5))*pow(((1-sqrt(5))/(2)),n)

    return int(equation)


print('Ile wyrazów mam wypisać?')   #pobranie od użytkownika ile wyrazów ciągu wypisać
n = int(input())

print("\nCiąg pierwszy:\n")     #ciąg pierwszy
for i in range(1,n+1):
    print("Wyraz",i,"wynosi:",fun1(i))

print("\nPorównanie wyniku numerycznego i analitycznego", n,"wyrazu ciągu pierwszego:")
print(fun1_2(n), end='')
if fun1(n) == fun1_2(n):
    print(' =',fun1(n))
else:
    print(' !=',fun1(n))

print("\nCiąg drugi:\n")        #ciąg drugi
for i in range(1,n+1):
    print("Wyraz",i,"wynosi:",fun2(i))

print("\nPorównanie wyniku numerycznego i analitycznego", n,"wyrazu ciągu drugiego:")
print(fun2_2(n), end='')
if fun2(n) == fun2_2(n):
    print(' =',fun2(n))
else:
    print(' !=',fun2(n))

print("\nCiąg trzeci:\n")       #ciąg trzeci
for i in range(1,n+1):
    print("Wyraz",i,"wynosi:",fun3(i))

print("\nPorównanie wyniku numerycznego i analitycznego", n,"wyrazu ciągu trzeciego:")
print(fun3_2(n), end='')
if fun3(n) == fun3_2(n):
    print(' =',fun3(n))
else:
    print(' !=',fun3(n))