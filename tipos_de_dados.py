''' utiliza 3 aspas para digitar
comentarios em bloco
para varias linhas enquanto # para uma linha
'''

# imprimindo dados no python com comando <print>
print(10+5+155-12)
print(1.3+8-3.8)
print(True)
print(False)
print("python")

# tipos de variaveis no python
int()
float()
str()
bool()

# exemplos do uso de variaveis
age = 13
name = 'agenor'
print(f'meu nome é {name} e eu tenho {age} anos de idade') # para concatenar strings com variaveis comece com f e chaves nas variaveis

# uma variavel constante por convenção é escrita em maiúscula
NOMECONSTANTEMAIUSCULA = 3.41
BRASILIAN_STATES = ["SP","RJ","BA"]
print(NOMECONSTANTEMAIUSCULA,BRASILIAN_STATES)


# exemplo de conversão de tipo de variaveis no python
preco = 10
print(preco)

preco = float(preco)
print(preco)

preco = str(preco)
print(preco)

print(int("10"))
print(int(11.4))
print(str(11.45))
print(float("45.6"))

valor = 100
valor_str = str(valor)
print(type(valor))
print(type(valor_str))
print (10 / 2)
print (10 // 2)

# entrada de dados no python com o <input>
nome = input("Informe o seu nome: ")
idade = input("informe a sua idade: ")

print (nome, idade) # no python por padrão cria-se um espaço entre as variaveis
print (nome, idade, end="...\n") # o <end> coloca um texto ao final da impressão e o \n quebra linha
print (nome, idade, sep="#", end="...\n")
print (nome, idade, sep="#") # o <sep> troca o espaço entre as variaveis para o texto especificado