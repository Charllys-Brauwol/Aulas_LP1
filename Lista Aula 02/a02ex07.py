'''7 - Escreva uma função que receba a idade do usuário e indique 
se ele pode ou não encher a cara de cachaça.'''

#input recebedo a idade
age = int(input('Vamos saber se você já pode beber.\nQual sua idade?\n'))

def age_drink(age):
    if age >= 18:
        print ('Parabéns! Você pode escolher.')
    else:
        print ('Não ainda.')
    return

x = age_drink (age)