# Carta de Amor
# Bibliotecas e outras dependencias
from datetime import date

def AboutLib():    
    AnoAtual = date.today().year
    SoftwareName = "GZUIS/CARTA DE AMOR"
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

def LCFunc():
    print("="*80)
    print(f'{Space} >> Carta de Amor <<')
    print("="*80)
    print()
    print("A biblia é como uma carta de amor de Deus")
    print("Para todas as criaturas, inclusive, para você")
    print()
    print("Para entender melhor o que acabamos de afirmar:")
    Nome = str(input("Digite o seu nome e leia: "))
    print()
    print(f'>> "Por que Deus amou {Nome} de tal maneira que deu o seu Filho unigênito, para que {Nome} ao nele crer não pereça mas tenha vida eterna"')
    print(">> João 3:16")
