# faça um programa que leia um angulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse angulo

# import math
from math import sin, cos, tan, radians
ang = float(input('Informe um angulo: '))

# Para calculo do Seno, Cosseno e Tangente o angulo deve ser em radianos

s = sin(radians(ang))
print('O SENO de {} é {:.2f}'.format(ang, s))
c = cos(radians(ang))
print('O COSENO de {} é {:.2f}'.format(ang, c))
t = tan(radians(ang))
print('A TANGENTE de {} é {:.2f}'.format(ang, t))


