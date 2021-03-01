# Faça um algoritmo que leia o salário de um funcionario e
# mostre seu novo salario, com 15% de aumento.

salario = float(input('Informe o salario do funcionário:'))
aumento = salario + (salario * 15 / 100)
print('O salário do funcionário que era de R${:.2f}, com aumento de 15% será de R${:.2f}'.format(salario, aumento))
