# Faça um algoritimo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto

preco = float(input('Informe o preço do produto R$:'))
desconto = preco - (preco * 5 / 100)
print('O produto que era R${:.2f}, com 5% de desconto será de R${:.2f}'.format(preco, desconto))
