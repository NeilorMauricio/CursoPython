from datetime import date

anoAtual = date.today().year #IMPORT-Qual o ano atual?
anoNascimento = int(input('Data de nascimento?'))
idade = anoAtual - anoNascimento
if idade < 18:
    tempo = 18 - idade
    print(f'Você ainda tem {idade} anos e falta {tempo} anos para se alistar ')
    ano = anoAtual + tempo
    print(f'Seu ano de alistamento será em {ano}')
elif idade >= 18 and idade <= 19:
    print(f'Você tem {idade} e pode se alistar')
else:
    tempo = idade - 18
    print (f'Você tem {idade} anos e passou {tempo} anos do tempo de alistamento')
    ano = anoAtual - tempo
    print(f'Seu ano de alistamento foi em {ano}')