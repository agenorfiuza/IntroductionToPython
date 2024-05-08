'''
Identar código é uma forma de manter o código fonte mais legível e manutenível. Mas em Python ela exerce um segundo papel, através da indentação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

As linguagens de programação costumam utilizar caracteres ou palavras reservadas para terminar o início e fim do bloco. Em Java e C por exemplo, utilizamos chaves:

Utilizando espaços

Existe uma convenção em Python, que define as boas práticas para escrita de código na linguagem. Nesse documento é indicado utilizar 4 espaços em branco por nível de indentação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.

Obrigação de identar o código

No python vc é obrigado a identar o código pois caso isso não seja feito o interpretador não vai rodar o código e vai ler como um erro.

'''
# Identação e Bloco de comando em Python

def sacar(self, valor: float) -> None:  # início do bloco do método
        
        if self.saldo >= valor:  # início do bloco do if

            self.saldo -= valor

        # fim do bloco do if

# fim do bloco do método

# exemplo de bloco de identação em python
def sacar(self, valor: float) -> None:
    if self.saldo >= valor:
        self.saldo -= valor


def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        print("valor sacado!")
        print("retire seu dinheiro na boca do caixa.")
    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
     saldo = 500
     saldo += valor
     print(saldo)

sacar(1000)

sacar(500)

depositar(300)