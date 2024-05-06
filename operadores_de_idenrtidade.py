'''
São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.

'''

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
#>>> True

curso is not nome_curso
#>>> False

saldo is limite
#>>> True

saldo = 1000
limite = 500

print(saldo is limite)
#>>> True

print(saldo is not limite)
#>>> False

saldo = 1000
limite = 1000

print(saldo is limite)
#>>> True

print(saldo is not limite)
#>>> False


