# Bibliotecas
from datetime import date
import Palavra

def AboutLib():
    AnoAtual = date.today().year
    SoftwareName = "GZUIS/DATE TIME"
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

# Variáveis Globais
Day = str(date.today().day)
Month = str(date.today().month)
Year = str(date.today().year)

UserDay = str(date.today().day)
UserMonth = str(date.today().month)
UserYear = str(date.today().year)

# Formatação de data
FormatDay = str()
FormatMonth = str()
FormatYear = str()
DateFormat = str()
Space = "                     "

# Teste de Modulo - Descomentar essa parte para executar os testes
## Day = str("15")
## Month = str("11")
## Year = str("2021")

# Teste de Saída - Output
## print()
## print(Day)
## print(type(Day))
## print(Month)
## print(type(Month))
## print(Year)
## print(type(Year))
## print()

def Today():
    # Variaveis Locais
    Today.intDay = int(Day)
    Today.intMonth = int(Month)
    Today.intYear = int(Year)
    print()

# Tipos de saida - Descomentar essa parte para executar os testes
##    print(Today.intDay)
##    print(type(Today.intDay))
##    
##    print(Today.intMonth)
##    print(type(Today.intMonth))
##
##    print(Today.intYear)
##    print(type(Today.intYear))
    
    # Processamento de formato de data (DD/MM/AAAA)
    if Today.intDay < 10 and len(Day) == 2:
        FormatDay = str(Day)
    else:
        if Today.intDay < 10 and len(Day) == 1:
            FormatDay = str('0') + str(Day)
        else:
            FormatDay = Day

    if Today.intMonth < 10 and len(Month) == 2:
        FormatMonth = str(Month)
    else:
        if Today.intMonth < 10 and len(Month) == 1:
            FormatMonth = str('0') + str(Month)
        else:
            FormatMonth = Month            

    # Saida da função
    DateFormat = str(f'{FormatDay}/{FormatMonth}/{Year}')
    print(">> Data da Consulta: ", DateFormat)

def UserDate():
    # Variaveis Locais
    UserDate.intDay = int(UserDay)
    UserDate.intMonth = int(UserMonth)
    UserDate.intYear = int(UserYear)
    print()

# Tipos de saida - Descomentar essa parte para executar os testes
##    print(Today.intDay)
##    print(type(Today.intDay))
##    
##    print(Today.intMonth)
##    print(type(Today.intMonth))
##
##    print(Today.intYear)
##    print(type(Today.intYear))

    # Processamento de formato de data (DD/MM/AAAA)
    if UserDate.intDay < 10 and len(str(UserDay)) == 2:
        FormatDay = str(UserDay)
    else:
        if UserDate.intDay < 10 and len(str(UserDay)) == 1:
            FormatDay = str('0') + str(UserDay)
        else:
            FormatDay = UserDay

    if UserDate.intMonth < 10 and len(str(UserMonth)) == 2:
        FormatMonth = str(UserMonth)
    else:
        if UserDate.intMonth < 10 and len(str(UserMonth)) == 1:
            FormatMonth = str('0') + str(UserMonth)
        else:
            FormatMonth = UserMonth

    # Saida da função
    DateFormat = str(f'{FormatDay}/{FormatMonth}/{UserYear}')
    
    print("="*80)
    print(f'{Space} >> Palavra do dia {DateFormat} <<')
    print("="*80)
