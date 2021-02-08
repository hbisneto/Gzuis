# Bibliotecas e outras dependencias
import Palavra
import LoveCard
from datetime import date
AnoAtual = date.today().year
SoftwareName = "GZUIS"
Version = "1.0"
CopyrightName = "Heitor Bisneto."
Space = "                     "
print("="*80)
print(f'[{SoftwareName}] - Em Execução...')
print("="*80)
print("Nome:", SoftwareName)
print("Versão:", Version)
print("Criado por:", CopyrightName)
if AnoAtual == 2021:
    print("Copyright ©", AnoAtual, "|", CopyrightName, "All rights reserved.")
else:
    print("Copyright © 2021 -", AnoAtual, "|", CopyrightName, "All rights reserved.")
print("")

MatrizOpc = ['LOVECARD', 'DWORD']
Count = int()
AboutItem = str()
Space = "                     "
UserInput = int()

# Funções de comandos

def CartaAmor():
    LoveCard.LCFunc()

def PalavraDia():
    print("="*80)
    print(f'{Space} >> Palavra do dia <<')
    print("="*80)
    Palavra.Process()
    
def MyApp():
    # Input do usuário:
    Opc = int(input(f'<{SoftwareName}/Opção:> <{SoftwareName}/'))
    UserInput = Opc
    
    if UserInput == 1:
        CartaAmor()
    elif UserInput == 2:
        PalavraDia()

# Lista de comandos
print("="*80)
print(f'{Space} >> Digite o número da opção desejada <<')
print("="*80)
print("             COMANDO                    FUNÇÃO DO COMANDO")
print("="*80)

for i in MatrizOpc:
    Count = Count + 1
    
    if Count == 1:
        AboutItem = f'{Space} Abrir função "Carta de amor"'
    elif Count == 2:
        AboutItem = f'{Space} Abrir função "Palavra do Dia"'
        
    print(f'<{SoftwareName}/{Count}> {i}{AboutItem}')
    
print("="*80)

MyApp()
