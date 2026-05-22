from utils.func import funcoes as func
from utils.tools import errors as error

opcao = 1 

recorde = {1 : None, 2 : None, 3 : None}

recordef = None
recordem = None
recorded = None
while opcao:
    func.menu()

    try:
        opcao = int(input("\nInsira a dificuldade de jogo: "))
    
    except ValueError: 
        print("[Log Error] - O sistema aceita apenas números inteiros")
        continue
    
    if opcao == 1:
        tentativas = 0
        limite = 50
        numero_sec = func.sortear(limite)
        print(f"\nSussurro: Tenta o número {numero_sec}!\n")
        flag = False
        historico = []

        if recorde[opcao]:
            print(f"Recorde de tentativas do modo fácil: {recorde[opcao]} tentativa(s)")

        while tentativas <= 4:
            if historico:
                print(f"\nTentativas Anteriores: {historico}")

            try:
                palpite = func.palpite(limite)
                if palpite is None:
                    continue

            except error.NumeroForaIntervaloError as e:
                print(e)
                continue

            if palpite == numero_sec:
                tentativas += 1
                print(f"Parabens! Você acertou com {tentativas} tentativa(s)!")
                flag = True
                if recorde[opcao] is None or tentativas < recorde[opcao]:
                    recorde[opcao] = tentativas
                break 
            
            elif palpite <= 0:
                print("\nSaindo do jogo atual...")
                flag = True
                break

            else:
                tentativas += 1
                historico.append(palpite)
                historico.sort()
                print(func.dicas(palpite, numero_sec))

        if not flag:
            print("\nVocê ultrapassou o número máximo de tentativas!\n")

    elif opcao == 2:
        tentativas = 0
        limite = 100
        numero_sec = func.sortear(limite)
        print(f"\nSussurro: Tenta o número {numero_sec}!")
        flag = False
        historico = []

        if recorde[opcao]:
            print(f"Recorde de tentativas do modo médio: {recorde[opcao]} tentativa(s)")

        while tentativas <= 9:
            if historico:
                print(f"\nTentativas Anteriores: {historico}")

            try:
                palpite = func.palpite(limite)
                if palpite is None:
                    continue
            except error.NumeroForaIntervaloError as e:
                print(e)
                continue
            if palpite == numero_sec:
                tentativas += 1
                print(f"Parabens! Você acertou com {tentativas} tentativa(s)!")
                flag = True
                if recorde[opcao] is None or tentativas < recorde[opcao]:
                    recorde[opcao] = tentativas
                break 
            
            elif palpite <= 0:
                print("\nSaindo do jogo atual...")
                flag = True
                break

            else:
                tentativas += 1
                historico.append(palpite)
                historico.sort()
                print(func.dicas(palpite, numero_sec))

        if not flag:
            print("\nVocê ultrapassou o número máximo de tentativas!\n")
    
    elif opcao == 3:
        tentativas = 0
        limite = 200
        numero_sec = func.sortear(limite)
        print(f"\nSussurro: Tenta o número {numero_sec}!")
        flag = False
        historico = []

        if recorde[opcao]:
            print(f"Recorde de tentativas do modo difícil: {recorde[opcao]} tentativa(s)")

        while tentativas <= 14:
            if historico:
                print(f"\nTentativas Anteriores: {historico}")

            try:
                palpite = func.palpite(limite)
                if palpite is None:
                    continue
            except error.NumeroForaIntervaloError as e:
                print(e)
                continue
            if palpite == numero_sec:
                tentativas += 1
                print(f"Parabens! Você acertou com {tentativas} tentativa(s)!")
                flag = True
                if recorde[opcao] is None or tentativas < recorde[opcao]:
                    recorde[opcao] = tentativas
                break 
            
            elif palpite <= 0:
                print("\nSaindo do jogo atual...")
                flag = True
                break

            else:
                tentativas += 1
                historico.append(palpite)
                historico.sort()
                print(func.dicas(palpite, numero_sec))

        if not flag:
            print("\nVocê ultrapassou o número máximo de tentativas!\n")
    
    elif opcao > 3:
        print("[Log Error] - Opção inválida: Insira uma das opções do menu!")

    else:
        print("\nSaindo do jogo...")
        print("======================================")
        break