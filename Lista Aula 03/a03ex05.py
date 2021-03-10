'''5 - Faça um programa para escrever a contagem regressiva do lançamento de um foguete.
O programa deve imprimir 10, 9, 8..., 1, 0 e "Fogo!", na tela Kite'''

import time

number = 10
seconds = 10

while seconds >= 0:
    time.sleep(1)
    print(f'Falta {seconds} para o lançamento.')
    seconds = seconds - 1

print('\n')
print('Lançamento autorizado. 🚀')