a = int(input('Primeiro valor:\n'))
b = int(input('Segundo valor:\n'))
c = int(input('Terceiro valor:\n'))
#Verificando o menor
menor = a
if b < a and b < c:
    menor = b
    if c < a and c < b:
        menor = c

        #Verificando o maior
        maior = a
        if b > a and b > c:
            maior = b
            if c > a and c > b:
                maior = c
                print(f'O menor valor é {menor}')
                print(f'O maior valor é {maior}')