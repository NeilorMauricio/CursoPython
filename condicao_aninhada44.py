precoNormal = float(input('Qual valor do produto?\n'))
condPagamento = float(input('Digite [1] para pagamento no dinheiro ou PIX.\n'
                            'Digite [2] para pagamento no cartão à vista\n'
                            'Digite [3] para pagamento até 2x no cartão\n'
                            'Digite [4] para pagamento 3x ou mais no cartão'))

if condPagamento == 1:
    precoAvista = precoNormal * 0.90
    print(f' DINHEIRO ou PIX: 10% de desconto. TOTAL R${precoAvista:.2f}')
elif condPagamento == 2:
    precoCartao = precoNormal * 0.95
    print(f'CARTÃO À VISTA: 5% de desconto. TOTAL R${precoCartao:.2f}')
elif condPagamento == 3:
    precoNormal = precoNormal
    print(f'ATÉ 2X NO CARTÃO: Preço normal. TOTAL R${precoNormal:.2f}')
elif condPagamento == 4:
    preco3X = precoNormal + precoNormal * 0.20
    print(f'3X OU MAIS NO CARTÃO: 20% de juros. TOTAL R${preco3X:.2f}')
else:
    print('Opção inválida. DIGITE A OPÇÃO DE  1 A 4')










