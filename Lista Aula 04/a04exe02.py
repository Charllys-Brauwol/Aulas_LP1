'''2 - No Basquete os lances podem valer três pontuações diferentes.
Finalização dentro do garrafão(2 pontos), finalização fora do garrafão (3 pontos),
cobrança de falta(1 ponto).
Faça uma função que receba a quantidade
de finalização de cada tipo e retorne quantos pontos no total o time fez.
Já que os valores dos pontos são fixos, utilize parâmetros opcionais.
Construa outra função que recebe os mesmos dados equivalente ao time adversário,
e em seguida crie uma terceira função que receba a primeira e a 
segunda como parâmetro e retorne o time vencedor'''


'''Atribuição do total de cestas do time da casa'''
ll_casa = int(input('Quantos cestas de lance livre o time da casa fez? \t'))
dpts_casa = int(input('Quantos cestas de 2 pontos o time da casa fez?\t\t'))
tpts_casa = int(input('Quantos cestas de 3 pontos o time da casa fez?\t\t'))

'''Função referente aos pontos do time da casa'''
def total_pontos_casa(ll_casa, dpts_casa, tpts_casa, lance_livre = 1, dois_pontos = 2, tres_pontos = 3):
    total_casa = (ll_casa*lance_livre) + (dpts_casa*dois_pontos) + (tpts_casa*tres_pontos)
    return total_casa

print(f'\nO total de pontos da equipe da casa foi: \t\t{total_pontos_casa(ll_casa, dpts_casa, tpts_casa)} pontos.')

'''Atribuição do total de cestas do time de fora'''
ll_fora = int(input('Quantos cestas de lance livre o time de fora fez?\t'))
dpts_fora = int(input('Quantos cestas de 2 pontos o time de fora fez?\t\t'))
tpts_fora = int(input('Quantos cestas de 3 pontos o time de fora fez?\t\t'))

'''Função referente aos pontos do time da casa'''
def total_pontos_fora(ll_fora, dpts_fora, tpts_fora, lance_livre = 1, dois_pontos = 2, tres_pontos = 3):
    total_fora = (ll_fora*lance_livre) + (dpts_fora*dois_pontos) + (tpts_fora*tres_pontos)
    return total_fora

print(f'\nO total de pontos da equipe de fora foi: \t\t{total_pontos_fora(ll_fora, dpts_fora, tpts_fora)} pontos.')

'''Função para comparar e retornar o time vencendor'''
def vencendor (total_pontos_fora, total_pontos_casa):
    if total_pontos_casa > total_pontos_fora:
        print('O time da casa Venceu!')
    elif total_pontos_casa == total_pontos_fora:
        print('Os times Empataram!')
    else:
        print('O time de fora Venceu!')

vencendor (total_pontos_fora(ll_fora, dpts_fora, tpts_fora), total_pontos_casa(ll_casa, dpts_casa, tpts_casa))