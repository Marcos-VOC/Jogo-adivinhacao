#Isso importa uma biblioteca nativa de python de randomização de elementos
import random

#Faz a atribuição a numero_sec de um número inteiro aleatório entre 1 e 50
numero_sec = random.randint(1, 50) 

print(f"Sussurro: Tenta o número {numero_sec}!")

#Número de tentativas
tentativas = 0

#Flag de verificação de vitória
flag = False


#Número máximo de tentativas é 3
while tentativas <= 2: 
    try:
        palpite = int(input("\nInsira seu palpite (de 1 a 50): "))

        #Caso o usuário insira algo que não seja um número
    except ValueError: 
        print("Valor inválido: É necessário um número entre 1 e 50!") 
        continue

    #Registra uma tentativa 
    tentativas +=1

    #Acerto
    if palpite == numero_sec:
        print(f"Parabens! Você acertou com {tentativas} tentativa(s)!")

        #Verifica que você ganhou e desabilita mensagem de derrota
        flag = True 

        #Para o while (laço de repetição)
        break 
    
    #Caso o usuário erre o número secreto
    else:
        diferenca = abs(palpite - numero_sec)

        #Temperatura: Quente, Morno, Frio ou Muito frio (proximidade)
        if diferenca <= 5:
            temp = "Quente - Você está quase lá!"
        elif diferenca <= 10:
            temp = "Morno - Falta um pouco mais!"
        elif diferenca <= 20:
            temp = "Frio - Está no caminho certo, mas falta algo!"
        else:
            temp = "Muito frio - Está um pouco longe do correto..."

        #Mais alto ou mais baixo
        if palpite < numero_sec:
            direcao = "O número secreto é mais alto!"
        else:
            direcao = "O número secreto é mais baixo!"
        
        print(f"Temperatura: {temp} | Proximidade: {direcao}")


#Verifica que o usuário ganhou e não mostra mensagem de derrota
if not flag:
    print("\nVocê ultrapassou o número máximo de tentativas!\n")

#Mensagem de finalização do programa
print("Saindo do programa...")