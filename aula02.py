#identação
    # Os 04 espaços delimitam hierarquicamente blocos de códigos.



#Definição de palavras compostas
    '''
     minhaNotaSemanal = 7.0 - Camel Case
     MinhaNotaSemanal = 7.0 - Pascal Case
     minha_nota_semanal = 7.0 - Snake Case
    '''

# Comentários em linhas únicas
''' Comentários em
várias linhas. '''

# Entrada de Dados - input
    ''' 
    OBS: colocando o tipo antes de input ele converte pro formato desejado.
    OBS: função type imprime o tipo de dado
    OBS: o input sempre devolve uma string
    '''

    nome = input("Nome: ")
    idade = int(input ("Idade: "))
    altura = float(input("Altura: "))
    
    print (type(nome))
    print (type(idade))
    

#Saída de dados - print
    '''
    OBS: estudar mais sobre a função format
    '''
    print ("Meu nome é: ", nome)
    print ("Meu nome é {}".format(nome))
    #fstring
    print(f"Meu nome é {nome} e eu tenho {idade} anos")
    