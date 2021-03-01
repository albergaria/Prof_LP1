# importo toda a biblioteca math - opção 1
# import math

# posso importar somente algumas funções da biblioteca - opção 2
from math import sqrt, floor, ceil

num = int(input('Digite um número:'))

# opção 1
# raiz = math.sqrt(num)

# opção 2
raiz = sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# Arredonda pra cima o numero
# opção 1
# math.ceil(raiz)

# opção 2
# ceil(raiz)

# Arredonda pra baixo o numero
# opção 1
# math.floor(raiz)

# opção 2
# floor(raiz)
