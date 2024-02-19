print('-=' * 20)
print('Analizador de triângulo')
print('-=' * 20)

r1 = float(input('Raio 1:'))
r2 = float(input('Raio 2:'))
r3 = float(input('Raio 3:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo', end='')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Não é triângulo')



