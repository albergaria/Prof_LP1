#   + adição        - subtração         * multiplicação     / divisão
#  ** potência     // divisão inteira   % resto da divisão
#  raiz quadrada **(1/2)                Raiz cubica **(1/3)

print('Operadores aritiméticos!')
print('--------------------------')
n1=float(input('Digite um número:'))
n2=float(input('Digite outro número:'))
print('--------------------------')
print('Adição dos números {} e {} é igual a: {}' .format(n1, n2, n1+n2))
print('Subtração dos números {} e {} é igual a: {}' .format(n1, n2, n1-n2))
print('Multiplicação dos números {} e {} é igual a: {}' .format(n1, n2, n1*n2))
print('Divisão dos números {} e {} é igual a: {}' .format(n1, n2, n1/n2))
print('O numero {} elevado a potência {} é igual a {}' .format(n1, n2, n1**n2))
print('A divisão inteira entre {} e {} é igual a {}' .format(n1, n2, n1//n2))
print('O resto da divisão inteira entre {} e {} é igual a {}' .format(n1, n2, n1 % n2))
