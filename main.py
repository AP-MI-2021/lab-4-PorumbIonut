import math
from math import sqrt

def citire_lista():
    lst = []
    n = int (input("Dati numarul de elemente din lista: "))
    for i in  range(0, n):
        x = int(input(f"dati elementul de pe pozitia {i}: "))
        lst.append(x)
    return lst

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def list_without_prime_nr(lista: list[int]):
    rezult_list = []
    lg = len(lista)
    for i in range(0, lg):
        if is_prime(lista[i]) == 0:
            rezult_list.append(lista[i])
    return rezult_list

def test_list_without_prime_nr():
    assert list_without_prime_nr([8, 19, 17, 25]) == [8, 25]

test_list_without_prime_nr()

def media_aritmetica(lista, n):
    ma = 0
    nr = 0
    sum = 0
    for i in lista:
        sum = sum + i
        nr = nr + 1
    ma = sum // nr
    if ma > n:
        return True
    return False


def test_media_aritmetica():
    assert media_aritmetica([10, -3, 25, -1, 3, 25, 18], 10) == 1

test_media_aritmetica()

def divizori_proprii(n):

    nrdiv = 0
    for i in range (2, n // 2 + 1):
        if n % i == 0:
            nrdiv = nrdiv + 1
    return nrdiv

def lista_cu_divizoriproprii(lista):
    rezult_list = []
    for i in lista:
        rezult_list.append(i)
        rezult_list.append(divizori_proprii(i))
    return rezult_list

def test_lista_cu_divizoriproprii():
    assert lista_cu_divizoriproprii( [19, 5, 24, 12, 9]) == [19, 0, 5, 0, 24, 6, 12, 4, 9, 1]

test_lista_cu_divizoriproprii()

def frecventa_numar(lista, el_lista):
    frec = 0
    for i in lista:
        if i == el_lista:
            frec = frec + 1
    return frec


def lista_tuplu(lista):
    rezult_list = []
    lg = len(lista)
    for i in range(0, lg):
        nr = lista[i]
        frecv = frecventa_numar(lista, nr)
        rezult_list.append((nr, i, frecv))
    return rezult_list
    
def test_lista_tuplu():
    assert lista_tuplu([25, 13, 26, 13]) == [(25, 0, 1), (13, 1, 2), (26, 2, 1), (13, 3, 2)]

test_lista_tuplu()

def main():
    shouldRun = True
    while(shouldRun):
        optiune = input("Alegeti numarul problemei pe care vreti sa o rezolvati: ")
        if optiune == "1":
            print("Cititi lista! /n")
            citire_lista()
        elif optiune == "2":
            lst = citire_lista()
            print("Rezolvati problema 2: Afișarea listei după eliminarea numerelor prime din listă ")
            print(list_without_prime_nr(lst))
        elif optiune == "3":
            lst = citire_lista()
            print("Rezolvati problema 3: Să se afișeze dacă media aritmetică a numerelor este mai mare decât un număr n dat. \n")
            nr = int(input("Dati un numar: "))
            if media_aritmetica(lst, nr) == 1:
                print("DA!")
            else:
                print("NU!")
        elif optiune == "4":
            lst = citire_lista()
            print("Rezolvati problema 4: ")
            print(lista_cu_divizoriproprii(lst))
        elif optiune == "5":
            lst = citire_lista()
            print("Rezolvati problema 5: ")
            print(lista_tuplu(lst))
        elif optiune == "x":
            print("Ati inchis meniul!")
            shouldRun = False
        else:
            print("Optiune gresita! Reincercati!")
main()