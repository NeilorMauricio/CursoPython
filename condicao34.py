salario = float(input('Qual salário do colaborador?\n'))
if salario <= 1250.00:
    aumento = salario + (salario * 0.15)
    print(f'O salário do colaborador com aumento de 15% foi de {aumento:.2f}\n')
else:
    aumento = salario + (salario * 0.10)
    print(f'O salário do colaborador com aumento de 10% foi de {aumento:.2f}\n')


