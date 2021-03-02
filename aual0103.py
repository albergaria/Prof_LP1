import math

numero = float(input('Digite um numero inteiro: '))

# raiz quadrada
#raiz = numero ** (1/2)

# Calcula a raiz quadrada utilizando a biblioteca math e a função sqrt
raiz = math.sqrt(numero)
print('A raiz quadrada de {} é {:.2f}'.format(numero, raiz))

# Calcula o seno utilizando a biblioteca math e a função sin
seno = math.sin(numero)
print('O seno de {} é {:.2f}'.format(numero, seno))

arredonda_cima = math.ceil(numero)
print('O numero {} arredondado para cima é igual a {}'.format(numero, arredonda_cima))

arredonda_baixo = math.floor(numero)
print('O numero {} arredondado para baixo é igual a {}'.format(numero, arredonda_baixo))

# funçoes da biblioteca math
# https://docs.python.org/pt-br/3/library/math.html?highlight=math#module-math

# Biblioteca que chama pygame
# https://www.pygame.org/news





