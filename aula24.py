"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Nicolas'
preco = 10000.908908
variavel = '%s o total é R$%.4f' % (nome,preco)
print(variavel )
print('O hexadecimal de %d é %x' % (1500,1500))