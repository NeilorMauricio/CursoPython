# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações sobre ele.

a = input('Digite algo')
print(type(a))
print(a.isalnum())
print(a.istitle())
print(a.isupper())
print(a.islower())
print(a.isnumeric())
print(a.isdecimal())
print(a.isdigit())
print(a.isalpha())
print(a.isspace())
print(a.isprintable())
print(a.isidentifier())

"""
isalnum – Verifique se todos os caracteres no texto são alfanuméricos
isalpha – Verifique se todos os caracteres no texto são letras
isascii – Verifique se a sequência é composta por todos os caracteres ASCII ou se a sequência estiver vazia também retornara true
isdecimal – Verifique se todos os caracteres no objeto unicode são decimais
isdigit – Verifique se todos os caracteres no texto são dígitos
isidentifier – Verifique se a sequência é um identificador válido :: O método isidentifier () retornará True se a string for um identificador válido, caso contrário, False. Uma sequência é considerada um identificador válido se contiver apenas letras alfanuméricas (a-z) e (0-9) ou sublinhados (_). Um identificador válido não pode começar com um número ou conter espaços.
islower – Verifique se todos os caracteres do texto estão em minúsculas
isnumeric – Verifique se todos os caracteres no texto são numéricos
isprintable – Verifique se todos os caracteres no texto são imprimíveis
isspace – Verifique se todos os caracteres no texto são espaços em branco
istitle – Verifique se cada palavra começa com uma letra maiúscula
isupper – Verifique se todos os caracteres do texto estão em maiúsculas
"""


