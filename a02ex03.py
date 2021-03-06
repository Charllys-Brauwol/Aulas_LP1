'''3 - Crie uma função que retorne o resto da divisão
do resultado da função da questão anterior por 2'''

def exerc02 ():

    number_one = int(input('Digite o primeiro número:'))
    number_two = int(input('Digite o segundo número:'))
    
    result = ((number_one*2)*(number_two*3))
    
    print (f'O valor é {result}.')

    return result

def division (result):
    value = result % 2

    print (f'O valor é: {value}.')