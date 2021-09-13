def inicio():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("               Médias Escolares               ")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

def input_media(pos):
    text = ['primeira', 'segunda', 'terceira', 'quarta']
    media = input(f"Insira a {text[pos]} nota:")

    try:
        media = float(media)
        if 0 <= media <= 10:
            return media
        else:
            print("Valor inválido. A média informada deve ser entre 0 e 10!")

    except:
        print("Valor inválido. A média informada deve ser numérica, sem espaços e com um ponto (.) para decimais!")


def main():
    inicio()

    i = 0
    notas = []

    while i < 4:
        media_individual = input_media(i)
        if isinstance(media_individual, float):
            notas.append(media_individual)
            i += 1

    soma = sum(notas)
    status = ['Aprovado', 'Reprovado', 'Em recuperação', 'Erro']
    media_final = round(soma / 4, 1)

    sts = 3
    if soma == 0 or media_final < 4:
        sts = 1
    elif 4 <= media_final < 6:
        sts = 2
    elif media_final >= 6:
        sts = 0

    print('\n')
    print("*** Resultado ***")
    print(f"| {notas[0]} | {notas[1]} | {notas[2]} | {notas[3]} | -> {media_final} -> Status: {status[sts]}")

if __name__ == '__main__':
    main()