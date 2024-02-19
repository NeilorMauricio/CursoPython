print('-=' * 20)
print('Analizador de triângulo')
print('-=' * 20)

r1 = float(input('Reta 1:\n'))
r2 = float(input('Reta 2:\n'))
r3 = float(input('Reta 3:\n'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r2 == r3:
        print('É Equilátero')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('É Isósceles')
    else:
        print('É Escaleno')

