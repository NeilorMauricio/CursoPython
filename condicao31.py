kmViagem = float(input('Qual a distância da sua viagem?'))
kmPreco = kmViagem * 0.5
kmDesconto = kmViagem * 0.4
if kmViagem <= 200:
    print(f'Você vai pagar R$: {kmPreco:.2f}')
else:
    print(f'Você vai pagar R$: {kmDesconto:.2f}')
