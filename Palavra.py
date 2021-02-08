# Bibliotecas e outras dependencias
from datetime import date
import DateTime
import ErrorReport

def AboutLib():
    AboutLib.SoftwareName = "GZUIS/PALAVRA DO DIA"
    Version = "1.0"

Space = "                     "
DAYS = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-Feira', 'Sexta-feira', 'Sábado', 'Domingo']
CrashMessage = lambda: print("O dado inserido é inválido. Execute o programa novamente.\n")

def Process():
    print(">> Os seguintes dados inseridos retornam valores de acordo com o dia, mês e ano")
    print(">> Insira um dado de cada vez:")
    try:
        Process.intDay = int(input(">> (2 digitos) Dia: "))
        DateTime.UserDay = Process.intDay

        Process.intMonth = int(input(">> (2 digitos) Mes: "))
        DateTime.UserMonth = Process.intMonth

        Process.intYear = int(input(">> (4 digitos) Ano: "))
        DateTime.UserYear = Process.intYear

        Process.Day = str(Process.intDay)
        Process.Month = str(Process.intMonth)
        Process.Year = str(Process.intYear)
        Process.MonthName = str()
    except:
        ErrorReport.DateInputError()

    try:
        Process.Date = date(year = Process.intYear, month = Process.intMonth, day = Process.intDay)
        Process.WeekIndex = Process.Date.weekday()
        Process.WeekDay = DAYS[Process.WeekIndex]
    except:
        CrashMessage()

    if Process.intDay < 1 or Process.intDay > 31:
        ErrorReport.DayError()
    if Process.intMonth < 1 or Process.intMonth > 12:
        ErrorReport.MonthError()
    if Process.intMonth == 1:
        Janeiro()

    elif Process.intMonth == 2:
        Fevereiro()

    elif Process.intMonth == 3:
        Marco()

    elif Process.intMonth == 4:
        Abril()

    elif Process.intMonth == 5:
        Maio()

    elif Process.intMonth == 6:
        Junho()
        
    elif Process.intMonth == 7:
        Julho()

    elif Process.intMonth == 8:
        Agosto()

    elif Process.intMonth == 9:
        Setembro()

    elif Process.intMonth == 10:
        Outubro()

    elif Process.intMonth == 11:
        Novembro()

    elif Process.intMonth == 12:
        Dezembro()
    else:
        CrashMessage()

def Config():
    AboutLib()
    Config.MonthName = str()
    Config.Message = str()
    Config.Vers = str()
    Config.Holiday = str()
        
def Output():
    DateTime.UserDate()
    
    print(f'>> Mensagem: {Config.Message}')
    print(f'>> Versiculo: {Config.Vers}')
    print(f'>> Feriado: {Config.Holiday}')
    DateTime.Today()
    print("="*80)

def Janeiro():
    Config()
    Config.MonthName = "Janeiro"
    if Process.intDay == 1:
        Config.Message = 'Respondendo Jesus: "Eu sou o caminho, a verdade e a vida. Ninguém vem ao Pai, a não ser por mim."'
        Config.Vers = "João 14:6"
        Config.Holiday = "Ano novo"
    elif Process.intDay == 2:
        Config.Message = 'Disse-lhe Jesus: "Eu sou a reissureição e a vida. \nAquele que crê em mim, ainda que morra, viverá;"'
        Config.Vers = "João 11:25"
        Config.Holiday = "Não"
    elif Process.intDay == 3:
        Config.Message = 'O Senhor te abençoe e te guarde; O Senhor faça resplanecer o seu rosto sobre ti e tenha misericórdia de ti; O Senhor sobre ti levante teu rosto e te dê a paz'
        Config.Vers = "Números 6:24-26"
        Config.Holiday = "Não"
    elif Process.intDay == 4:
        Config.Message = 'E Jesus disse: "Tenho-vos dito isso, para que em mim tenhais paz; No mundo tereis aflições, mas tende bom ânimo; Eu venci o mundo"'
        Config.Vers = "João 16:33"
        Config.Holiday = "Não"
    elif Process.intDay == 5:
        Config.Message = 'Bem aventurados os pacificadores, por que eles serão chamados filhos de Deus'
        Config.Vers = "Mateus 5:9"
        Config.Holiday = "Não"
    elif Process.intDay == 6:
        Config.Message = 'Deixo-vos a paz, a minha paz vos dou; Não vo-la dou como o mundo a dá. Não se turbe o vosso coração, nem se atemorize.'
        Config.Vers = "João 14:27"
        Config.Holiday = "Não"
    elif Process.intDay == 7:
        Config.Message = 'Pra quem quer amar a vida e ver os dias bons, refreie a sua língua do mal, e os seus labios não falem engano; Aparte-se do mal e faça o bem; Busque a paz e siga-a'
        Config.Vers = "1 Pedro 3:10-11"
        Config.Holiday = "Não"
    elif Process.intDay == 8:
        Config.Message = 'Em paz me deito e logo adormeço, pois só tu, Senhor, me fazes viver em segurança'
        Config.Vers = "Salmos 4:8"
        Config.Holiday = "Não"
    elif Process.intDay == 9:
        Config.Message = 'E a paz de Deus, para a qual também fostes chamado em um corpo, domine em vossos corações; E sede agradecidos.'
        Config.Vers = "Colossenses 3:15"
        Config.Holiday = "Não"
    elif Process.intDay == 10:
        Config.Message = 'Certamente ele tomou sobre si as nossas enfermidades e sobre si levou as nossas doenças, contudo nós o consideramos o castigado por Deus, por ele atingido e afligido.'
        Config.Vers = "João 14:6"
        Config.Holiday = "Não"

    Output()
    
def Fevereiro():
    Config()
    Config.MonthName = "Fevereiro"
    print("="*80)
    print(f'{Space} >> Mês de {Config.MonthName} não implementado <<')
    print("="*80)
    Config.Message = 'As mensagens do mês escolhido ainda não foram implementadas no sistema'
    Config.Vers = f'<{AboutLib.SoftwareName}/Exception>'
    Config.Holiday = "Reinicie o programa para pesquisar palavras do dia"

    Output()

def Marco():
    Config()
    Config.MonthName = "Março"
    print("="*80)
    print(f'{Space} >> Mês de {Config.MonthName} não implementado <<')
    print("="*80)
    Config.Message = 'As mensagens do mês escolhido ainda não foram implementadas no sistema'
    Config.Vers = f'<{AboutLib.SoftwareName}/Exception>'
    Config.Holiday = "Reinicie o programa para pesquisar palavras do dia"

    Output()
    
def Abril():
    Config()
    Config.MonthName = "Abril"
    print("="*80)
    print(f'{Space} >> Mês de {Config.MonthName} não implementado <<')
    print("="*80)
    Config.Message = 'As mensagens do mês escolhido ainda não foram implementadas no sistema'
    Config.Vers = f'<{AboutLib.SoftwareName}/Exception>'
    Config.Holiday = "Reinicie o programa para pesquisar palavras do dia"

    Output()

def Maio():
    Config()
    Config.MonthName = "Maio"
    print("="*80)
    print(f'{Space} >> Mês de {Config.MonthName} não implementado <<')
    print("="*80)
    Config.Message = 'As mensagens do mês escolhido ainda não foram implementadas no sistema'
    Config.Vers = f'<{AboutLib.SoftwareName}/Exception>'
    Config.Holiday = "Reinicie o programa para pesquisar palavras do dia"

    Output()
    
def Junho():
    Config()
    Config.MonthName = "Junho"
    print("="*80)
    print(f'{Space} >> Mês de {Config.MonthName} não implementado <<')
    print("="*80)
    Config.Message = 'As mensagens do mês escolhido ainda não foram implementadas no sistema'
    Config.Vers = f'<{AboutLib.SoftwareName}/Exception>'
    Config.Holiday = "Reinicie o programa para pesquisar palavras do dia"

    Output()

def Julho():
    Config()
    Config.MonthName = "Julho"
    print("="*80)
    print(f'{Space} >> Mês de {Config.MonthName} não implementado <<')
    print("="*80)
    Config.Message = 'As mensagens do mês escolhido ainda não foram implementadas no sistema'
    Config.Vers = f'<{AboutLib.SoftwareName}/Exception>'
    Config.Holiday = "Reinicie o programa para pesquisar palavras do dia"

    Output()
    
def Agosto():
    Config()
    Config.MonthName = "Agosto"
    print("="*80)
    print(f'{Space} >> Mês de {Config.MonthName} não implementado <<')
    print("="*80)
    Config.Message = 'As mensagens do mês escolhido ainda não foram implementadas no sistema'
    Config.Vers = f'<{AboutLib.SoftwareName}/Exception>'
    Config.Holiday = "Reinicie o programa para pesquisar palavras do dia"

    Output()

def Setembro():
    Config()
    Config.MonthName = "Setembro"
    print("="*80)
    print(f'{Space} >> Mês de {Config.MonthName} não implementado <<')
    print("="*80)
    Config.Message = 'As mensagens do mês escolhido ainda não foram implementadas no sistema'
    Config.Vers = f'<{AboutLib.SoftwareName}/Exception>'
    Config.Holiday = "Reinicie o programa para pesquisar palavras do dia"

    Output()
    
def Outubro():
    Config()
    Config.MonthName = "Outubro"
    print("="*80)
    print(f'{Space} >> Mês de {Config.MonthName} não implementado <<')
    print("="*80)
    Config.Message = 'As mensagens do mês escolhido ainda não foram implementadas no sistema'
    Config.Vers = f'<{AboutLib.SoftwareName}/Exception>'
    Config.Holiday = "Reinicie o programa para pesquisar palavras do dia"

    Output()

def Novembro():
    Config()
    Config.MonthName = "Novembro"
    print("="*80)
    print(f'{Space} >> Mês de {Config.MonthName} não implementado <<')
    print("="*80)
    Config.Message = 'As mensagens do mês escolhido ainda não foram implementadas no sistema'
    Config.Vers = f'<{AboutLib.SoftwareName}/Exception>'
    Config.Holiday = "Reinicie o programa para pesquisar palavras do dia"

    Output()
    
def Dezembro():
    Config()
    Config.MonthName = "Dezembro"
    print("="*80)
    print(f'{Space} >> Mês de {Config.MonthName} não implementado <<')
    print("="*80)
    Config.Message = 'As mensagens do mês escolhido ainda não foram implementadas no sistema'
    Config.Vers = f'<{AboutLib.SoftwareName}/Exception>'
    Config.Holiday = "Reinicie o programa para pesquisar palavras do dia"

    Output()
