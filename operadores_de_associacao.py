'''
São operadores utilizados para verificar se um objeto está presente em uma sequência .

Operador in = verifica se um objeto está presente em uma sequência.

Operador not in = verifica se um objeto não está presente em uma sequência.

Os operadores são case senssitive
'''

curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

print("Python" in curso)
#>>> True

print("maçã" not in frutas)
#>>> True

print(200 in saques)
#>>> False

print("curso" in curso)
#>>> False

print(1500 not in saques)
#>>> False