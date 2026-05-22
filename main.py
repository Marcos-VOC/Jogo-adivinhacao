from utils.func import funcoes as func
from utils.tools import errors as error

opcao = 1 
placar = func.Placar()

while opcao:
    func.menu()

    try:
        opcao = int(input("\nInsira a dificuldade de jogo: "))
    
    except ValueError: 
        print("[Log Error] - O sistema aceita apenas números inteiros")
        continue
    
    if opcao == 1:
        limite = 50
        tentativas_max = 5
        jogo = func.Jogo(limite, tentativas_max)
        print(f"\nSussurro: Tenta o número {jogo.numero_sec}!\n")
        flag = False

        placar.mostrar(opcao)

        while jogo.tentativas < jogo.tentativas_max:
            if jogo.historico:
                print(f"\nTentativas Anteriores: {jogo.historico}")

            try:
                palpite = jogo.palpite()
                if palpite is None:
                    continue

            except error.NumeroForaIntervaloError as e:
                print(e)
                continue

            if palpite == jogo.numero_sec:
                jogo.registrarpalpite(palpite)
                print(f"Parabens! Você acertou com {jogo.tentativas} tentativa(s)!")
                flag = True
                placar.atualizar(opcao, jogo.tentativas)
                break 
            
            elif palpite <= 0:
                print("\nSaindo do jogo atual...")
                flag = True
                break

            else:
                jogo.registrarpalpite(palpite)
                print(jogo.dicas(palpite))

        if not flag:
            print("\nVocê ultrapassou o número máximo de tentativas!\n")

    elif opcao == 2:
        limite = 100
        tentativas_max = 10
        jogo = func.Jogo(limite, tentativas_max)
        print(f"\nSussurro: Tenta o número {jogo.numero_sec}!")
        flag = False

        placar.mostrar(opcao)

        while jogo.tentativas < jogo.tentativas_max:
            if jogo.historico:
                print(f"\nTentativas Anteriores: {jogo.historico}")

            try:
                palpite = jogo.palpite()
                if palpite is None:
                    continue

            except error.NumeroForaIntervaloError as e:
                print(e)
                continue

            if palpite == jogo.numero_sec:
                jogo.registrarpalpite(palpite)
                print(f"Parabens! Você acertou com {jogo.tentativas} tentativa(s)!")
                flag = True
                placar.atualizar(opcao, jogo.tentativas)
                break 
            
            elif palpite <= 0:
                print("\nSaindo do jogo atual...")
                flag = True
                break

            else:
                jogo.registrarpalpite(palpite)
                print(jogo.dicas(palpite))

        if not flag:
            print("\nVocê ultrapassou o número máximo de tentativas!\n")
    
    elif opcao == 3:

        limite = 200
        tentativas_max = 15
        jogo = func.Jogo(limite, tentativas_max)
        print(f"\nSussurro: Tenta o número {jogo.numero_sec}!")
        flag = False

        placar.mostrar(opcao)
        while jogo.tentativas < jogo.tentativas_max:
            if jogo.historico:
                print(f"\nTentativas Anteriores: {jogo.historico}")

            try:
                palpite = jogo.palpite()
                if palpite is None:
                    continue

            except error.NumeroForaIntervaloError as e:
                print(e)
                continue

            if palpite == jogo.numero_sec:
                jogo.registrarpalpite(palpite)
                print(f"Parabens! Você acertou com {jogo.tentativas} tentativa(s)!")
                flag = True
                placar.atualizar(opcao, jogo.tentativas)
                break 
            
            elif palpite <= 0:
                print("\nSaindo do jogo atual...")
                flag = True
                break

            else:
                jogo.registrarpalpite(palpite)
                print(jogo.dicas(palpite))

        if not flag:
            print("\nVocê ultrapassou o número máximo de tentativas!\n")
    
    elif opcao > 3:
        print("[Log Error] - Opção inválida: Insira uma das opções do menu!")

    else:
        print("\nSaindo do jogo...")
        print("======================================")
        break