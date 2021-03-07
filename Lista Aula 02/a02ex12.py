'''12 - Esreva uma função que receba a medida do raio e 
calcule a área e perímetro de uma circuferência.'''

print('Vamos calcular a área de uma circuferência:')

raio = float(input('Informe o raio da circunferência:\n'))

def perimeter_calculation(raio):
    area_value = float(3.14 * (raio ** 2))
    print(f'A área é igual: {area_value}%.2f')
    perimeter = float(2 * 3.14 * raio)
    print(f'O perímetro é igual: {perimeter}%.2f')
    return area_value, perimeter
