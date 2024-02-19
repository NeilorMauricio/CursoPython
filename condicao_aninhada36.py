valorCasa = float(input('Qual o valor da casa?'))
salario = float(input('Qual seu salário?'))
anos = int(input('Quantos anos você quer pagar?'))
prestacao = valorCasa / (anos * 12)
print(f'Para pagar a casa em {anos} anos, você terá uma prestação de R${prestacao:.2f}')
if prestacao > salario * 0.30:
    print('Você não pode pagar a casa com esse salário!')
elif prestacao <= salario * 0.30:
    print('Parabéns, você pode comprar sua casa!')

