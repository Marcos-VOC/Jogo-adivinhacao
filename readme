# 🎯 Jogo de Adivinhação

Jogo de adivinhação de números desenvolvido em Python, com sistema de dicas de temperatura (quente/frio), histórico de palpites, placar de recordes e três níveis de dificuldade. Projeto desenvolvido com foco no aprendizado de fundamentos da linguagem, incluindo estruturas de controle, tratamento de exceções, modularização e introdução à orientação a objetos.

---

# 🕹️ Como funciona

O jogador escolhe uma dificuldade e tenta adivinhar um número sorteado aleatoriamente dentro de um intervalo definido. A cada tentativa errada, o jogo fornece duas informações:

- **Temperatura** — indica a proximidade do palpite em relação ao número secreto (quente, morno, frio ou muito frio)
- **Direção** — indica se o número secreto é maior ou menor que o palpite

O jogador vence se acertar o número dentro do limite de tentativas da dificuldade escolhida. Ao sair, o jogo exibe o melhor resultado (menor número de tentativas) registrado em cada dificuldade durante a sessão.

---

# ⚙️ Modos de jogo

| Modo    | Intervalo | Tentativas |
|---------|-----------|------------|
| Fácil   | 1 a 50    | 5          |
| Médio   | 1 a 100   | 10         |
| Difícil | 1 a 200   | 15         |

> Digite `0` durante uma partida para abandoná-la e voltar ao menu.

---

# 📁 Estrutura do projeto

```
jogo-adivinhacao/
│
├── main.py                  # Ponto de entrada e fluxo principal do jogo
│
└── utils/
    ├── func/
    │   └── funcoes.py       # Funções do jogo: menu, sorteio, palpite e dicas
    └── tools/
        └── errors.py        # Exceções customizadas
```

---

# 🧠 Conceitos aplicados

## Estruturas de controle
Uso de `while`, `if`, `elif`, `else`, `break` e `continue` para controlar o fluxo do jogo — incluindo loops de menu, loops de tentativas e saída antecipada de partidas.

## Funções
O código é dividido em funções com responsabilidade única (`menu`, `sortear`, `palpite`, `dicas`), seguindo o princípio de separação de responsabilidades e evitando repetição de lógica.

## Tratamento de exceções
Uso de `try/except` de forma cirúrgica — cobrindo apenas as linhas que podem falhar por razões esperadas, como a conversão de entrada do usuário com `int(input())`. Segue a prática de *narrow except*, capturando exceções específicas (`ValueError`) em vez de blocos genéricos.

## Exceções customizadas
Criação de `NumeroForaIntervaloError`, uma exceção própria que herda de `Exception`, utilizada para sinalizar quando o jogador insere um número fora do intervalo válido da dificuldade escolhida — separando erros de tipo (letras) de erros de domínio (número fora do intervalo).

## Listas
Uso de lista para registrar o histórico de palpites de cada partida, com ordenação via `.sort()` para exibição em ordem crescente a cada rodada.

## Dicionários
Uso de dicionário para mapear cada dificuldade ao seu recorde de tentativas (`{1: None, 2: None, 3: None}`), substituindo três variáveis separadas por uma estrutura centralizada.

## Modularização
O projeto é dividido em módulos com responsabilidades distintas: `main.py` controla o fluxo, `funcoes.py` contém a lógica do jogo e `errors.py` centraliza as exceções. Os módulos se comunicam via importações explícitas.

---

# ▶️ Como executar

**Pré-requisitos:** Python 3.8 ou superior instalado.

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/jogo-adivinhacao.git

# Entre na pasta
cd jogo-adivinhacao

# Execute o jogo
python main.py
```

---

# 📌 Observações de desenvolvimento

Este projeto foi construído de forma incremental, começando com um script simples e evoluindo gradualmente:

1. Lógica básica de sorteio e comparação
2. Loop de tentativas com `while`
3. Dicas de temperatura e direção
4. Tratamento de entradas inválidas com `try/except`
5. Separação em funções e módulos
6. Exceção customizada para validação de intervalo
7. Histórico de palpites com listas
8. Placar de recordes por dificuldade com dicionário

---

# 🛠️ Melhorias futuras

- Refatoração com orientação a objetos (classes `Jogo` e `Placar`)
- Persistência do placar entre sessões com arquivos `.json`
- Interface gráfica com `tkinter` ou `pygame`