'''3 - Crie uma função que retorne o resto da divisão
do resultado da função da questão anterior por 2'''

number_one = int(input('Digite o primeiro número:\n'))
number_two = int(input('Digite o segundo número:\n'))

#Função da questão 02
def exerc02 (number_one, number_two):
    
    result = ((number_one*2)*(number_two*3))
    
    print (f'O valor é: \n{result}.')

    return result

#Função de retorno da divisão
def total (exerc02):
    result = exerc02 (number_one, number_two)
    value = result % 2
    return (value)

#Print do valor
print (f'O resto dadivisão por 2 é: \n{total(exerc02)}.')