from random import randint
computador = randint(0,5) #Faz o PC "PENSAR"
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' *20)
jogador = int(input('Em que número eu pensei?')) #Jogador tenta adivinhar
if computador == jogador:
    print('Parabéns, você acertou!')
    print('-=-' *20)
else:
    print(f'Que pena, você errou! Eu pensei no número {computador} e não no número {jogador}')
    print('-=-' *20)


