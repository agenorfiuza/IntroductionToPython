# Exemplo

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque)
#>>> True

print(saque <= limite)
#>>> False

# Operador E

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque and saque <= limite)
#>>> False

# Operador OU

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque or saque <= limite)
#>>> True

# Operador Negação

contatos_emergencia = []

print(not 1000 > 1500)
#>>> True

print(not contatos_emergencia)
#>>> True

print(not "saque 1500;")
#>>> False

print(not "")
#>>> True

# Parênteses

saldo = 1000
saque = 250
limite = 200
conta_especial = True

print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)
#>>> True

print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))
#>>> True