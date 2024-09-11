"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
print(1234)
print(456)
#int('a')

numero = input('Vou dobrar o seu numero: ')

try:
    numero_float = float(numero)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')