# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triangulo retangulo (um dos angulos igaul a 90° e calcule o comprimento da hipotenusa

from math import hypot

co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))

# hi = (co ** 2 + ca ** 2) ** (1/2) # opcao 1
hi = hypot(co, ca)  # opcao 2

print('A hipotenusa do triangulo retangulo é {:.2f}'.format(hi))
