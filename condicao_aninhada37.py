num = int(input('Digite um número inteiro:'))
print('Escolha uma das bases para conversão:\n'
      '[1] Binário\n'
      '[2] Octal\n'
      '[3] Hexadecimal\n')
opcao = int(input('Sua opção:'))
if opcao == 1:
    print(f'{num} convertido para binário é igual a {bin(num)[2:]}')
    print('-=' * 20)
elif opcao == 2:
    print(f'{num} convertido para octal é igual a {oct(num)[2:]}')
    print('-=' * 20)
elif opcao == 3:
    print(f'{num} convertido para Hexadecimal é igual a {hex(num)[2:]}')
    print('-=' * 20)
else:
    print('Opção inválida!DIGITE A OPÇÃO 1, 2 OU 3')


