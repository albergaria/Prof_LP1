# Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar. Considere US$1,00 = R$5,47

din = float(input('Informe quanto você tem na carteira em R$:'))
cotacao = 5.47
dolar = din/cotacao
print('Com R${:.2f} você consegue comprar US${:.2f} com a cotação de R${}'.format(din, dolar, cotacao))

# Calcular em euros tbm.

