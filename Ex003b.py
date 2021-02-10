# Formatacao dos dados no print.
# Diferença entre número e string

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
soma = n1 + n2
print('A soma dos dois numeros é:', soma)
print('A soma dos dois numeros é: {}'.format(soma))

print('A soma de ', n1, 'e', n2, 'é igual a', soma)
print('A soma de {} e {} é igual a {}' .format(n1, n2, soma))
