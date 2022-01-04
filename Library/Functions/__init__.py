from time import sleep
from pojetos.Functions import *

valor = 0


def qtdcadastro():
    while True:
        try:
            valor = int(input("\033[33m Quantos livros serão cadastrados? \033[m "))
            if valor>0:
                break
            if valor == 0 or valor <= 0:
                print("Por favor, digite uma numeração válida")
                continue
        except (ValueError,TypeError):
            print("Digite um numero, por favor")
    return valor