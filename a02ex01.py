'''1 - Converta as seguintes expressões matemáticas para que possam ser calculadas usando Python:
10 + 20 x 30
4² / 3
(9⁴ + 2) x 6 -1
(9⁴ + 2)⁴ + ( 10 / 1)'''

print ('Primeira expressão: 10 + 10 x 30')

number_one = 10
number_two = 30

result = number_one + (number_one * number_two)

print (f'O resultado é: {result}\n')

print ('Segunda expressão: 4² / 3')

number_one = 4
number_two = 3

result = ((number_one ** 2) / number_two)

print (f'O resultado é: {result}\n')

print ('Terceira expressão: (9⁴ + 2) x 6 -1')

number_one = 9
number_two = 2
number_three = 6
number_four = 1

result = (((((number_one ** 4) + number_two) * number_three) - number_four))

print (f'O resultado é: {result}\n')

print ('Quarta expressão: (9⁴ + 2)⁴ + ( 10 / 1)')

number_one = 9
number_two = 2
number_three = 10
number_four = 1

result = (((number_one ** 4) + number_two) + (number_three / number_four))

print (f'O resultado é: {result}\n')