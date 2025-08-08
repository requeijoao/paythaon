import random
import time

comidas = ["🍕", "🍔", "🍟", "🍗", "🍣", "🍉"]
pares = comidas * 2
random.shuffle(pares)

tabuleiro = ["❓"] * 12
descobertos = [False] * 12

def mostrar_tabuleiro():
    for i in range(0, 12, 4):
        linha = ""
        for j in range(4):
            idx = i + j
            if descobertos[idx]:
                linha += f"{pares[idx]}  "
            else:
                linha += f"{tabuleiro[idx]}  "
        print(f"{i:2} {i+1:2} {i+2:2} {i+3:2}")
        print(linha)
        print()

def jogo_acabou():
    return all(descobertos)

print("🎮 Bem-vindo ao Jogo da Memória - Tema Comidas! 🎮")
tentativas = 0

while not jogo_acabou():
    mostrar_tabuleiro()
    try:
        escolha1 = int(input("Escolha a primeira carta (0 a 11): "))
        escolha2 = int(input("Escolha a segunda carta (0 a 11): "))

        if escolha1 == escolha2 or not (0 <= escolha1 < 12) or not (0 <= escolha2 < 12):
            print("❌ Escolha inválida. Tente novamente.\n")
            continue

        if descobertos[escolha1] or descobertos[escolha2]:
            print("❌ Uma das cartas já foi revelada. Tente novamente.\n")
            continue

        # Mostra temporariamente
        print("\n✨ Revelando cartas:")
        tabuleiro[escolha1] = pares[escolha1]
        tabuleiro[escolha2] = pares[escolha2]
        mostrar_tabuleiro()
        time.sleep(1)

        if pares[escolha1] == pares[escolha2]:
            print("✅ Par encontrado!\n")
            descobertos[escolha1] = True
            descobertos[escolha2] = True
        else:
            print("❌ Não foi um par. Tente novamente.\n")
            tabuleiro[escolha1] = "❓"
            tabuleiro[escolha2] = "❓"

        tentativas += 1

    except ValueError:
        print("❌ Entrada inválida. Digite um número entre 0 e 11.\n")

print(f"🎉 Parabéns! Você completou o jogo em {tentativas} tentativas.")

