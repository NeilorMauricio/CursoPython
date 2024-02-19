velocidade = float(input('Qual a velocidade?'))
multa = (velocidade - 60) * 7
if velocidade >= 60:
    print(f'Você está acima da velocidade permitida. A MULTA É DE {multa:.2f} brl')
else:
    print('Você está abaixo da velocidade permitida')
