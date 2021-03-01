# Exibir um texto na tela
print('Boa noite!')

# Receber uma informação do usuario. Exibe o texto e fica esperando um retorno
input('Informe um numero:')

# Receber uma informação do usuario. Exibe o texto e fica esperando um retorno
# Guarda o valor em uma variavel n1
n1 = input('Informe um numero:')

# Definir o tipo da variavel
# int()   - numeros inteiros sem casa decimal. Ex.: 7, -4, 0, 9875
# float() - numeros com casas decimais. Ex.: 4.5, 0.076, -15.223, 7.0
n1 = int(input('Informe um numero:'))
n2 = int(input('Informe um numero:'))

# Exibe o conteudo da variavel
print('O numero informado foi: {}'.format(n1))

print('O Resultado de {} + 15 = {}'.format(n1, (n1 + 15)))

# Adicao
s = n1 + n2
print('{} + {} = {}'.format(n1, n2, s))

# Subtração
sub = n1 - n2
print('{} - {} = {}'. format(n1, n2, sub))

# Multiplicação
m = n1 * n2
print('{} * {} = {}'.format(n1, n2, m))

# Divisão
d = n1 / n2
print('{} / {} = {}'.format(n1, n2, d))

# Divisão inteira
di = n1 // n2
print('{} // {} = {}'.format(n1, n2, di))

# Resto da divisão
r = n1 % n2
print('{} % {} = {}'.format(n1, n2, r))

# Potencia
p = n1 ** n2
print('{} ** {} = {}'.format(n1, n2, p))

# Raiz quadrada
rq = n1**(1/2)
print ('A Raiz quadrada de {} é {}'.format(n1, rq))

# Raiz cubica
rc = n1**(1/3)
print ('A Raiz cubica de {} é {}'.format(n1, rc))

# Sequencia de operadores aritimeticos
# 1 => ()
# 2 => **
# 3 => * / // %
# 4 => + -

# Com base na sequencia acima o resultado será:
n3 = int(input('Informe um numero:'))

print(n1 + (n2 * n3))
