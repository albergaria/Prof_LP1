# Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

ni = int(input('Informe um numero inteiro:'))

print('A tabuada de {} é: '.format(ni))
print('-'*20)
print('{} x {:2} = {}'.format(ni, 1, ni*1))
print('{} x {:2} = {}'.format(ni, 2, ni*2))
print('{} x {:2} = {}'.format(ni, 3, ni*3))
print('{} x {:2} = {}'.format(ni, 4, ni*4))
print('{} x {:2} = {}'.format(ni, 5, ni*5))
print('{} x {:2} = {}'.format(ni, 6, ni*6))
print('{} x {:2} = {}'.format(ni, 7, ni*7))
print('{} x {:2} = {}'.format(ni, 8, ni*8))
print('{} x {:2} = {}'.format(ni, 9, ni*9))
print('{} x {:2} = {}'.format(ni, 10, ni*10))
print('-'*20)
print('')
print('A tabuada de {} é: '.format(ni))
print('='*20)
print(' {} x  1 = {:2} \n {} x  2 = {:2} \n {} x  3 = {:2} \n {} x  4 = {:2} \n {} x  5 = {:2} \n {} x  6 = {:2} \n {} x  7 = {:2} \n {} x  8 = {:2} \n {} x  9 = {:2} \n {} x 10 = {:2}'.format(ni, (ni*1), ni, (ni*2), ni, (ni*3), ni, (ni*4), ni, (ni*5), ni, (ni*6), ni, (ni*7), ni, (ni*8), ni, (ni*9), ni, (ni*10)))
print('='*20)
