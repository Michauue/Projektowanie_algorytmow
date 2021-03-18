def fun1(n):
    if n == 0:
        return 0
    else:
        equation = int(pow(3,n)+fun1(n-1))

    return equation


def fun1_2(n):                              #analitycznie funkcja pierwsza
    equation = 0
    for i in range(1,n+1):
        equation = equation + int(pow(3,i))

    return equation


def fun2(n):
    if n == -1 or n == 0:
        return 0
    else:
        equation = int(n+fun2(n-2))

    return equation


def fun2_2(n):
    equation = 0

    return equation


def fun3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    else:
        equation = int(fun3(n - 1)+fun3(n-2))

    return equation


print('Ile wyrazów mam wypisać?')   #pobranie od użytkownika ile wyrazów ciągu wypisać
n = int(input())

print("\nCiąg pierwszy:\n")     #ciąg pierwszy
for i in range(1,n+1):
    print("Wyraz",i,"wynosi:",fun1(i))

print("\nPorównanie wyniku numerycznego i analitycznego", n,"wyrazu ciągu:")
print(fun1_2(n), end='')
if fun1(n) == fun1_2(n):
    print(' =',fun1(n))
else:
    print(' !=',fun1(n))

print("\nCiąg drugi:\n")        #ciąg drugi
for i in range(1,n+1):
    print("Wyraz",i,"wynosi:",fun2(i))

print("\nCiąg trzeci:\n")       #ciąg trzeci
for i in range(1,n+1):
    print("Wyraz",i,"wynosi:",fun3(i))