# Nessa aula, vamos aprender operações com String no Python.
# As principais operações que vamos aprender são:

# Existe a diferenca entre maiusculas e minusculas

# mensagem = input('Digite um texto:')

# no Python ele faz diferença entre letras maiusculas e minusculas

# print(mensagem.replace('R','W'))
# trocar a letra informada por outra desejada

# print(mensagem.capitalize())
# coloca a primeira letra da frase em maiuscula

# print(mensagem.title())
# coloca a primeira letra de cada palavra da frase em maiuscula

# print(mensagem.upper())
# coloca toda a frase em maiusculas

# print(mensagem.lower())
# coloca toda a frase em minuscculas

# mensagem2 = input('Digite um texto2:')
# print(mensagem + ' de ' + mensagem2)
# Ao trabalhar com texto o sinal de + (concatenar)


# Catalão
# CATALAO
# CATALÃO
# CAtalao

# Usar capitalize
# Catalão
# Catalao
# Catalão
# Catalao

# Replace('ã', a)
# Catalao
# Catalao
# Catalao
# Catalao

# Trabalhando com partes de texto
mensagem = 'COTEC CATALAO'

print(mensagem[3])
# retornar o caractere na posicao
# E

print(mensagem[4:10])
# retorna os caracteres da posicao inicial até uma antes da final
# C CATA

print(mensagem[6:12:2])
# retorna os caracteres da posicao inicial até uma antes da final de 2 em 2 posições
# CTL

print(mensagem[:7])
# retornar os caracteres da posição 0 até a posição desejada
# COTEC C

print(mensagem[7:])
# retornar os caracteres da posição desejada até o final
# ATALAO

print(mensagem[3::4])
# retorna os caracteres da posicao desejada até a posição final de 4 em 4 posições
# EAA
