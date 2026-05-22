import random
from utils.tools import errors as erros

def menu():
    print("\n======================================")
    print("         Jogo da advinhação\n")
    print("1 - Fácil (1 a 50 | 5 tentativas)")
    print("2 - Médio (1 a 100 | 10 tentativas)")
    print("3 - Difícil (1 a 200 | 15 tentativas)")
    print("0 - Sair do programa")

def sortear(limite):
    numero_sec = random.randint(1, limite)
    return numero_sec


def palpite(limite):
    try:
        palpite = int(input("Insira seu palpite: "))
    
    except ValueError:
        print("[Log Error] - O sistema aceita apenas números inteiros!")
        return None
    
    if palpite > limite:
        raise erros.NumeroForaIntervaloError("[Log Error] - Você inseriu um número fora do intervalo definido.")


    return palpite

def dicas(palpite, numero_sec):
    diferenca = abs(palpite - numero_sec)

    if diferenca <= 5:
        temp = "Quente - Você está quase lá!"
        
    elif diferenca <= 10:
        temp = "Morno - Falta um pouco mais!"
        
    elif diferenca <= 20:
        temp = "Frio - Está no caminho certo, mas falta algo!"
        
    else:
        temp = "Muito frio - Está um pouco longe do correto..."
        

    if palpite < numero_sec:
        direcao = "O número secreto é mais alto!"
    else:
        direcao = "O número secreto é mais baixo!"

    result = (f"Temperatura: {temp} | Proximidade: {direcao}")

    return result