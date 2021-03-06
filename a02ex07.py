'''7 - Escreva uma função que receba a idade do usuário e indique 
se ele pode ou não encher a cara de cachaça.'''

age = int(input('Qual sua idade?\n'))

if (age >= 18):
    print ('Parabéns! Você pode escolher.')
else:
    print ('Não ainda.')