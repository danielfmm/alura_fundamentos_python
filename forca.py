import random

def jogar():

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 7

    imprime_msg_de_abertura(tentativas)
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(imprime_letras_formatadas(letras_acertadas))


    while not enforcou and not acertou:

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros, tentativas)


        enforcou = erros == tentativas
        acertou = "_" not in letras_acertadas
        print(imprime_letras_formatadas(letras_acertadas))

    if acertou:
        imprime_msg_vencedor()
    else:
        imprime_msg_perdedor(palavra_secreta)


def imprime_msg_de_abertura(tentativas):
    print("**************************")
    print("Bem-vindo ao jogo da Forca")
    print("**************************")
    print(f"Acerta a palavra para ganhar! Você pode chutar até {tentativas} vezes.")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r", encoding="UTF-8")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    return palavras[numero].upper()


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute_do_jogador = input("Qual letra? ")
    chute_do_jogador = chute_do_jogador.strip().upper()
    return chute_do_jogador


def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = chute
        index += 1


def imprime_msg_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_msg_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros, tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    tentativas_restantes = tentativas - erros
    if tentativas_restantes > 0:
        plural_ou_singular = "tentativas" if tentativas_restantes > 1 else "tentativa"
        print(f"Você ainda tem {tentativas_restantes} {plural_ou_singular}.")



def imprime_letras_formatadas(acertadas):
    letras_acertadas_formatadas = ""
    for letra in acertadas:
        letras_acertadas_formatadas = f"{letras_acertadas_formatadas} {letra}"
    return f"| {letras_acertadas_formatadas[1:]} |"


if __name__ == '__main__':
    jogar()
