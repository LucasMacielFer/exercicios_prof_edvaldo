class Caixa:
    def __init__(self):
        self.__fichas = 1000

    def vender(self, numero):
        if self.__fichas >= numero > 0:
            try:
                self.__fichas -= int(numero)
            except:
                print("Insira um valor válido para venda!")
        else:
            print("O valor precisa ser maior que 0 e menor que o número de fichas em estoque!")

    def devolver(self, numero):
        if self.__fichas + numero <= 1000 and numero > 0:
            try:
                self.__fichas += int(numero)
            except:
                print("Insira um valor válido para venda!")
        else:
            print("O valor precisa ser maior que 0 e não deve totalizar, junto às fichas em estoque, mais que 1000!")

    def __str__(self):
        return f"Fichas em estoque: {self.__fichas}"


if __name__ == "__main__":
    Caixa_geral = Caixa()