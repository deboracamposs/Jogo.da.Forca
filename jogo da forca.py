import random
from biblioteca import animais, estados, nomes, comidas
print(' ▬▬ BEM VINDO AO JOGO DA FORCA ▬▬')
print(' Seu principal objetivo é acertar a palavra antes do bonequinho ser completado.\n Prepara-se para o desafio! \n QUE OS JOGOS COMECEM!')
loop = True
usuario = input("Digite seu nome: ")
vitorias = 0
derrotas = 0
alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
def boneco(chances):
    if chances == 6:
        return f"___\n"
    if chances == 5:
        return f"___\n   O\n\n"
    if chances == 4:
        return f"___\n   O \n   |\n"
    if chances == 3:
        return f"___\n   O \n  /|\n"
    if chances == 2:
        return f"___\n   O \n  /|\ \n"
    if chances == 1:
        return f"___\n   O \n  /|\\\n  / \n"
    if chances == 0:
        return f"___\n   O \n  /|\\\n  /\ \n"
def palavraOculta(palavra, acertos):
    resultado = ""
    for letra in palavra:
        if letra in acertos:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado
while loop:
    print('▬▬▬ VAMOS LÁ! ▬▬▬')
    palavras = animais + estados + nomes + comidas
    palavra = random.choice(palavras)
    palavras.remove(palavra)
    if palavra in animais:
        dica = "Dica: é um animal."
    if palavra in estados:
        dica = "Dica: é um estado."
    if palavra in nomes:
        dica = "Dica: é um nome."
    if palavra in comidas:
        dica = "Dica: é uma comida."
    chances = 6
    acertos = []
    erros = []
    while chances > 0:
        print(dica)
        print(f"{palavraOculta(palavra, acertos)}")
        print(f"Letras erradas: {', '.join(erros)}")
        while True:
            tentativa = input("• Digite uma letra: ").upper()
            c = 0
            for x in tentativa:
                if x not in alfabeto:
                    c += 2
                c += 1
            if c > 1:
                print("Você digitou mais de uma letra ou um caractere inválido. Tente novamente!")
            elif tentativa in acertos or tentativa in erros:
                print(f"A letra {tentativa} já foi digitada, tente novamente!")
            else:
                break
        if tentativa in palavra:
            acertos.append(tentativa)
            if all(letra in acertos for letra in palavra):
                print(f"Parabéns, você acertou! A palavra era: {palavra}.")
                vitorias += 1
                break
        else:
            erros.append(tentativa)
            chances -= 1
            print(f'Letra incorreta.')
        print(boneco(chances))
    if chances == 0:
        print(f'Você errou! A palavra era: {palavra}.')
        derrotas += 1
    questao = input('Deseja jogar novamente? (s/n): ')
    if questao.lower() == 'n':
        loop = False
print('Programa finalizado! Obrigado por jogar.')
print(f'Sua pontuação final foi de:\nVitórias: {vitorias}\nDerrotas: {derrotas}')


