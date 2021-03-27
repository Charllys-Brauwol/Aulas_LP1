'''8 - P = True e Q = False. 
Aplique De Morgan na seguinte proposição e atribua o valor a uma variável 
 ~(p ^ (p v q)), essa variável deve ser retornada partir de uma função'''


def morgan(P, Q):
    return (not(P or (P and Q)))
    
x= morgan(True,False)
print(x)