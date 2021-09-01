import random
from random import randrange

print("....:::: DADOS PYTHONICOS ::::....")

def condicionais(msg):
    if msg == 1:
        jogar = input("Jogar os dados?")
    if msg == 2:
        jogar = input("Deseja jogar novamente?")

    jogar = str(jogar).lower()
    sim = ["sim", "s", "si", "y", "yes"]

    def jogar_dados(qtd_dados):
        i = 1
        while i <= qtd_dados:
            numero = random.randrange(1,7)
            print(numero)
            i += 1

    def avalia():
        if sim.count(jogar) != 0:
            dados = input("Quantos dados jogar?")
            try:
                int(dados)

            except ValueError:
                print("Insira um número!")
                avalia()

            dados = int(dados)
            jogar_dados(dados)
            condicionais(2)


    avalia()

condicionais(1)






