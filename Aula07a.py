# Operadores aritimeticos

n1 = int(input('Informe o 1º numero:'))
n2 = int(input('Informe o 2º numero:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
# format o nro com 3 casas decimais :.3f
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('A divisão inteira é {} e a potência é {}'.format(di, p))

# Para colocar tudo na mesma linha após o format colocar , end=' '
# Para quebrar a linha em qualquer ponto basta colocar \n onde deseja a quebra de linha
print('A soma é {},\n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end=' ')
print('A divisão inteira é {} e a potência é {}'.format(di, p))
