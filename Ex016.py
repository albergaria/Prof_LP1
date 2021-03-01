# Crie um programa que leia um número real qualquer pelo teclado e
# mostre na tela a sua porção inteira.

# Exemplo: Digite um numero: 29.734
# O numero 29.734 tem a parte inteira igual a 29

'''
# opção 1
from math import trunc

numero = float(input('Digite um numero:'))
pi = trunc(numero)
print('A parte inteira de {} é {}'.format(numero, pi))
'''

# opção 2
numero = float(input('Digite um numero:'))
pi = int(numero)
print('A parte inteira de {} é {}'.format(numero, pi))