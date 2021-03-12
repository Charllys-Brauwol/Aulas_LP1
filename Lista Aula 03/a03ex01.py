'''
1 - Escreva uma função que simule o funcionamento de um radar eletrônico.
Essa função deve receber a velocidade do carro de um usuário. Caso ultrapasse 80 Km/h,
exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa,
cobrando R$ 90 reais pela infração + R$ 5 reais por km acima de 80 km/h
'''

velocity = int(input('Qual a velocidade que o carro estava em km/h?\n'))

def traffic_ticket(velocity):
    if (velocity > 80):
        total = (90.00 + ((velocity - 80) * 5.00))
        print(f'Ultrapassou o Limite.\nO total da multa foi: {total:.2f}.')
    else:
        print('Parabéns, não ultrapassou o limite de velocidade.')
    return
