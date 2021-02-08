# Error Report
# Bibliotecas e outras dependencias
from datetime import date

def AboutLib():
    AnoAtual = date.today().year
    SoftwareName = "GZUIS/ERROR REPORT"
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


def DayError():
    raise RuntimeError("\n\n>> Mensagem: O dia precisa ser um número maior que 0 e menor que 32\n")

def MonthError():
    raise RuntimeError("\n\n>> Mensagem: O mês precisa ser um número maior que 0 e menor que 13\n")

def DateInputError():
    raise RuntimeError("\n\n>> Mensagem: Existem algumas regras para a inserção de dados para datas\n- Tem que ser um número inteiro.\n- Para DIA, usar pelo menos um digito numérico.\n- Para MÊS, usar pelo menos um digito numérico.\n- Para ANO, usar pelo menos dois digitos numéricos\n\n>> Importante: O programa não parará a execução se o ANO for inserido com menos de dois digitos. Exceto se o tipo de entrada não for numérico")
