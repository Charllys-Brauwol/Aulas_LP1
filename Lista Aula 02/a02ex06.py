'''6 - Suponha que o preço de capa de um livro seja 24.95. 
Mas as livrarias recebem um desconto de 40%. 
O transporte custa 3.00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. 
Qual é o custo total de atacado para 60 copias?'''

#Valores declarados
book_cover = (24.95 * 0.4)
transport = (3.00 + (60*0.75))

#Função de calculo do valor total
def total_price (book_cover, transport):
    price = book_cover + transport
    return (price)

#Print da informação do valor dos 60 livros
print (f'O valor total dos 60 livros é igual: \n{total_price (book_cover, transport):.2f}')