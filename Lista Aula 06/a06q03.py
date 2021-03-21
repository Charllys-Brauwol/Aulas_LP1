'''
3 - Escreva uma função que receba uma lista com itens repetidos e retorne a mesma lista com itens únicos
'''

lista_01 = [1, 1, 2, 2, 3, 3, 4, 4]

def sem_repetir(lista_01):
    return set(lista_01)

print(sem_repetir(lista_01))