import random
import numpy as np

def somma(lista_numeri):
    res = 0
    for el in lista_numeri:
        try:
            res += el
        except:
            res="stringa non sommabile"
    return res

def generatore_num(quantita):
    numeri = []
    for el in range(quantita):
        numeri.append(random.randint(1,100))
    return numeri

def media(lista_dati):
    if len(lista_dati)!=0:
        x = len(lista_dati)
        sum = somma(lista_dati)
        res = sum/x
    else:
        res = "lista vuota"
    
    return res