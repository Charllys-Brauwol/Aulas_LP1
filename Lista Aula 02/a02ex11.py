'''11- Escreva um programa que receba as medidas dos lados de um triângulo e 
calcule sua área e perímetro.'''

print('Vamos calcular o Perímetro e a Área de uma Triângulo:')

#Recebendo as medidas do triângulo
one_side = float(input('Digite o tamanho do primeiro lado do triângulo:\n'))
two_side = float(input('Digite o tamanho do segundo lado do triângulo:\n'))
three_side = float(input('Digite o tamanho do terceiro lado do triângulo:\n'))
base = float(input('Digite o tamanho da base do triângulo:\n'))
height = float(input('Digite o tamanho da altura do triângulo:\n'))


#Função do Perímetro
def perimeter(one_side, two_side, three_side):
    return (one_side + two_side + three_side)

#Print do perímetro
print(f'O perímetro é: {perimeter(one_side, two_side, three_side)}')

#Função da Área
def area(base, height):
    return ((base * height) / 2)

#Print da área
print(f'A área é: {area(base, height)}')
