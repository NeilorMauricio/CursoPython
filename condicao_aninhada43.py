peso = float(input('Digite seu peso em kg:'))
altura = float(input('Digite sua altura em metros:'))
imc = peso / (altura ** 2)
print(f'Seu IMC é {imc:.1f}')
if imc < 18.5:
    print('Está abaixo do ideal')
elif imc <= 25:
    print('Está no ideal')
elif imc <= 30:
    print('Está com obesidade')
else:
    print('Está com obesidade mórbida')


