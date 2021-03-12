'''2 - Escreva uma função que receba dois números como argumento
 e retorne o produto do dobro do primeiro pelo triplo do segundo'''

#Input recebedo os números do tipo inteiro
number_one = int(input('Digite o primeiro número:\n'))
number_two = int(input('Digite o segundo número:\n'))

#Função do calculo 
def product(number_one, number_two):
    return ((number_one*2)*(number_two*3))

print (f'O valor é: \n{product(number_one, number_two)}.')
 
