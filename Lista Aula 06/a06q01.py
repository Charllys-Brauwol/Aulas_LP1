'''
1 - Faça uma função que receba duas listas e que gere uma terceira com os elementos das duas primeiras.
'''

lista_01 = [1, 2, 3, 4]
lista_02 = [5, 6, 7, 8]

def unir(lista_01, lista_02):
    lista_03 = list(lista_01+lista_02)
    return lista_03

print(unir(lista_01, lista_02))