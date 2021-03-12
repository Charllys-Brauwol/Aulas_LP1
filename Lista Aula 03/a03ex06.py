'''6 - Utilizando while imprima os resultados da tabuada de 2:
A saída deve ser semelhante a:
2 x 1 = 2
2 x 2 = 4
'''

print('Tabuada de 2:')

number = 0
multiplied = 0

while number < 10:
    print(f'2 x {number} = {multiplied}.')
    number += 1
    multiplied = (number * 2)