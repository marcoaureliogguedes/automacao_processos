Sistema de Automação de Processos

# Passo 1: Analisar e buscar as informações das ações

# Instalando bibliotecas
!pip install yfinance
!pip install pyautogui
!pip install pyperclip

# Importando bibliotecas
import yfinance as yf
import pyautogui 
import pyperclip
import time

# Armazenando os dados em uma variável
ticke = input("Digite o código da ação: ")
dados_acoes = yf.Ticker(ticker).history("6mo")

# Vizualizando os dados das ações
display(dados_acoes)

# Armazenando os dados da coluna de fechamento
fechamento = dados_acoes.Close
fechamento

# Passo 2: Criando as análises de dados
- Cotação Máxima
- Cotação Minima
- Cotação Atual

# Cotação Máxima
cotacao_maxima = round(fechamento.max(), 2)
cotacao_maxima

# Cotação Mínima
cotacao_minima = round(fechamento.min(), 2)

# Trabalhando com índice para pegar a cotação atual
cotacao_atual = round(fechamento[-1], 2)
cotacao_atual

# Imprimindo as cotações com um texto
print(f"A cotação máxima da ação foi de: R$ {cotacao_maxima}")
print(f"A cotação mínima da ação foi de: R$ {cotacao_minima}")
print(f"A cotação atual da ação foi de: {cotacao_atual}")

# Passo 3: Enviar um e-mail para o gestor com os resultados das análises
- abrir uma nova aba no navegador, atalho "(ctrl+t)"
- digitar o endereço do Gmail, "Enter"
- clicar no botão, "Escrever"
- digitar o destinatário, "Tab"
- digitar o assunto, "Tab"
- digitar a mensagem do E-mail "Mensagem"

# Pausar o python
pyautogui.PAUSE = 5

# Passo 1 - Abrir uma nova aba no navegador com o atalho (ctrl + t)
pyautogui.hotkey("ctrl", "t")

# Passo 2 - Digitar o endereço do gmail
pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

# Passo 3 - Clicar no botão (Escrever)
pyautogui.click(x=72, y-192)

# Passo 4 - Digitar o destinatário e dar um TAB
pyperclip.copy("mgaurelioguedes@gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Passo 5 - Digitar o assunto e dar um TAB
pyperclip.copy("Análises Diárias das Ações")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Passo 6 - Digitar a mensagem e e-mail
mensagem = f"""
Prezado Diretor,

Seguem as análises, conforme solicitado, da ação {ticker} referente aos últimos 6 meses:

Cotação máxima: R$ {cotacao_maxima}
Cotação mínima: R$ {cotacao_minima}
Cotação atual: R$ {cotacao_atual}

Qualquer dúvida, estou à disposição.

atenciosamente,

Marco Guedes

"""

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# time
time.sleep(5)

pyautogui.position()