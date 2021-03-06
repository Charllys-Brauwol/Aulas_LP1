'''5 - Escreva uma função que receba como argumento a quantidade de Km
percorridos por um carro alugado pelo usuário,
assim como a quantidade de dia pelos quais o carro foi alugado. 
A função deve retornar o preço a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.'''

number_of_days = int(input('Quantos dias você andou com o carro?\n'))
number_of_km = int(input('Quantos km você andou com o carro?\n'))



def pay (number_of_days, number_of_km):
    total_payment = ((number_of_days * 60.00) + (number_of_km * 0.15))

    return (total_payment)

print (f'Total que irá pagar: \n{pay(number_of_days, number_of_km):.2f}')
