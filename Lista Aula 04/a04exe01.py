'''1 - Escreva três funções sendo que: A Primeira deve receber uma quantidade de dias
e retornar o equivalente em horas.
A segunda deve receber a quantidade de horas retornada pela primeira função
e retornar o equivalente em minutos,
a terceira por sua vez recebe a quantidade de minutos da segunda e retorna 
o equivalente em segundos. Utilize as funções como parâmetros.'''

days = float(input('Digite o total de dias para conversão:'))

def days_to_hours(days):
    hours = float(days / 24)
    return hours

def hours_to_minutes(days_to_hours):
    minutes = float(days_to_hours / 60)
    return minutes

def minutes_to_seconds(hours_to_minutes):
    seconds = float(hours_to_minutes / 60)
    return seconds

print(f'A conversão de {days} dias é:\nHoras = {days_to_hours(days)}\nMinutos = {hours_to_minutes(days_to_hours)}\nSegundos = {minutes_to_seconds(hours_to_minutes)}')