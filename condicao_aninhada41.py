from datetime import date
anoAtual = date.today().year
dataNascimento = int(input('Data de nascimento?'))
idade = anoAtual - dataNascimento
if idade <= 9:
    print(f'Você tem {idade} anos e está na categoria MIRIM')
elif idade <= 14:
    print(f'Você tem {idade} anos e está na categoria INFANTIL')
elif idade <= 19:
    print(f'Você tem {idade} anos e está na categoria JÚNIOR')
elif idade <= 25:
    print(f'Você tem {idade} anos e está na categoria SÊNIOR')
else:
    print(f'Você tem {idade} anos e está na categoria MASTER')
