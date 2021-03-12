'''14 - Um fazendeiro cria Galinhas, Vacas e Porcos.
Escreva uma função que receba a quantidade de cada animal
que o fazendeiro possui atualmente e retorne quantas patas tem na fazenda.'''

#Input recebendo os dados do tipo inteiro
chickens = int(input('Quantas galinhas você têm?'))
cows = int(input('Quantas vacas você têm?'))
pigs = int(input('Quantas porcos você têm?'))

#Função com retorno do total de patas
def total_paws(chickens, cows, pigs):
    total = ((chickens * 2) + ((cows + pigs) * 4))
    return total

#Print do valor que a função retorna
print(f'O total de patas é:\n{total_paws(chickens, cows, pigs)}')