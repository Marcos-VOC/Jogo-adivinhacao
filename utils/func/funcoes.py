import random
from utils.tools import errors as erros


class Jogo:
    def __init__(self, limite, tentativas_max):
        self.limite = limite
        self.tentativas_max = tentativas_max
        self.numero_sec = random.randint(1, limite)
        self.tentativas = 0
        self.historico = []

    def palpite(self):
        try:
            palpite = int(input("Insira seu palpite: "))
        
        except ValueError:
            print("[Log Error] - O sistema aceita apenas números inteiros!")
            return None
        
        if palpite > self.limite:
            raise erros.NumeroForaIntervaloError("[Log Error] - Você inseriu um número fora do intervalo definido.")

        return palpite
    
    def dicas(self, palpite):
        diferenca = abs(palpite - self.numero_sec)

        if diferenca <= 5:
            temp = "Quente - Você está quase lá!"
            
        elif diferenca <= 10:
            temp = "Morno - Falta um pouco mais!"
            
        elif diferenca <= 20:
            temp = "Frio - Está no caminho certo, mas falta algo!"
            
        else:
            temp = "Muito frio - Está um pouco longe do correto..."
            

        if palpite < self.numero_sec:
            direcao = "O número secreto é mais alto!"
        else:
            direcao = "O número secreto é mais baixo!"

        result = (f"Temperatura: {temp} | Proximidade: {direcao}")

        return result
    
    def registrarpalpite(self, palpite):
        self.tentativas += 1
        self.historico.append(palpite)
        self.historico.sort()

class Placar:
    def __init__(self):
        self.recordes = {1 : None, 2: None, 3: None}
    
    def mostrar(self, opcao):
        if self.recordes[opcao] is not None:
            print(f"O histórico atual dessa dificuldade é de {self.recordes[opcao]} tentativa(s)!")

    def atualizar(self, opcao, tentativas):
        if self.recordes[opcao] is None or self.recordes[opcao] > tentativas:
            self.recordes[opcao] = tentativas


def menu():
    print("\n======================================")
    print("         Jogo da advinhação\n")
    print("1 - Fácil (1 a 50 | 5 tentativas)")
    print("2 - Médio (1 a 100 | 10 tentativas)")
    print("3 - Difícil (1 a 200 | 15 tentativas)")
    print("0 - Sair do programa")