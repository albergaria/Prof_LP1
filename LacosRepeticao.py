# While
# Quero mostrar na tela os numeros de 1 a 5

print(1)
print(2)
print(3)
print(4)
print(5)

contador = 1
while (contador < 6):
    print(contador)
    contador = contador + 1
print('Chegamos ao fim da repeticao')

# Verificar a identação do programa. No caso acima só vai executar a linha
# print('Chegamos ao fim da repeticao') quando sair do while.



# While else
contador = 0
while (contador < 5):
      print(contador)
      contador = contador + 1
else:
      print("O loop while foi encerrado com sucesso!")

# Break
x = 0
while x < 10:
    print(x)
    x += 1    # x = x + 1
    if x == 6:
        print("x é igual a 6")
        break # Sai de dentro do while
else:
    print("fim while")

# ---------------------------------------------------
# For
nomes = ['Pedro', 'João', 'Leticia']
for n in nomes:
     print(n)

numero = int(input('Digite um numero: '))
tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Tabuada de {}'.format(numero))
for n in tabuada:
    print('{} x {} = {}'.format(numero, n, (numero * n)))


# For ... else
nomes = ['Pedro', 'João', 'Leticia']
for n in nomes:
     print(n)
else:
     print("Todos os nomes foram listados com sucesso")
