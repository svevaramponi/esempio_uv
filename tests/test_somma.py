import pytest
from src.operazioni import somma

def test_somma_positiva():
    assert somma([10,20])==30

def test_somma_negativi():
    assert somma([10,-5,1])==6

def test_somma_lista_vuota():
    assert somma([])==0

def test_somma_stringhe():
    assert somma([1,"a"])== "stringa non sommabile"