'''4 - Escreva uma função para calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
Considere que um fumante perde 10 minutos de vida a cada cigarro,
a função deverá retornar quantos dias de vida um fumante perderá.
Exiba o total em dias.'''

quantity_cigarettes = float(input('Quantos cigarros você fuma por dia?'))
quantity_years = float(input('Quantos anos faz que você fuma?'))
print('\n')

def lost_minutes (quantity_cigarettes, quantity_years):
    return (quantity_cigarettes * 10 * quantity_years * 360)

amount = lost_minutes(quantity_cigarettes, quantity_years)

amount = amount / 60 / 24

print (f'O total de dias perdidos são: {amount:.0f} dias.')