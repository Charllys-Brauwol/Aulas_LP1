'''12 - Esreva uma função que receba a medida do raio e 
calcule a área e perímetro de uma circuferência.'''

print('Vamos calcular a área de uma circuferência:')

#Input recebendo os dados
raio = float(input('Informe o raio da circunferência:\n'))

#Funçao de calculo
def perimeter_calculation(raio):
    return (float(2 * 3.14 * raio))

print(f'O perímetro é igual: {perimeter_calculation(raio):.2f}')

def area_calculation(raio):
    return (float(3.14 * (raio ** 2)))

print(f'A área é igual: {area_calculation(raio):.2f}')
'''
print(f'A área é igual: {perimeter_calculation(raio):.2f}')
print(f'O perímetro é igual: {perimeter:.2f}')'''