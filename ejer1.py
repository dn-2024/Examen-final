
import random


def num_aleatorios():
    list_1 = []
    for _ in range(10):
        list_1.append(random.randint(1, 100))
    return list_1


def almacenar(lista):
    no_repetidos = list(set(lista))
    return no_repetidos


def ordenar(lista):
    orden = sorted(lista)
    return orden


def num_par(lista):
    maxi = max(lista)
    if maxi % 2 == 0:
        return maxi
