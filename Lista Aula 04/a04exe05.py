'''5- Escreva uma função para validar uma string.
Ela deve receber como argumento, uma string, o número minimo e máximo de 
caracteres e retornar VERDADEIRO se o número de caracteres da string 
estiver dentro do min e max passado, e FALSO caso contrário.'''

string = input('Digite uma frase entre 5 e 10 letras:\n')

quantidade = len(string)

def validar(string):
    if quantidade >= 5 and quantidade <=10:
        print(True)
    else:
        print(False)

validar(string)