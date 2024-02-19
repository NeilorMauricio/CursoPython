nota1 = float(input('Digite sua nota:'))
nota2 = float(input('Digite sua nota:'))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Reprovado \nSua média foi {media}')
elif media >= 5 and media <= 6.9:
    print(f'Recuperação \nSua média foi {media}')
else:
    print(f'Aprovado \nSua média foi {media}')
