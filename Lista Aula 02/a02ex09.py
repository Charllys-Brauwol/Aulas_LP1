'''9 - Crie uma função que receba duas strings e retorne True 
se o número de elementos de uma for igual ao da outra, 
e retorne False caso contrário.
Pesquise pelo método len() na documentação do Python.'''

print('Digite duas palavras e vamos ver se possuem a mesma quantidade de letras:')

#Input que receberá as duas strings
word_one = input('Digite a primeira palavra:\n')
word_two = input('Digite a segunda palavra:\n')

#Método len, que irá calcular a quantidade de letras de cada string
first_quantity = len(word_one)
second_quantity = len(word_two)

#Função de comparação
def compare_words(first_quantity, second_quantity):
    if (first_quantity == second_quantity):
        return True
    else:
        return False

#Print do resultado
print(f'O retorno foi: {compare_words(first_quantity, second_quantity)}')