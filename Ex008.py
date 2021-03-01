# Escreva um programa que leia um valor em metros
# e o exiba convertido em centimetros e milimetros

m = float(input('Informe o tamanho em metros:'))
print('{} metros é igual a {} centimetros e {} milimetros.'.format(m, (m*100), (m*1000)))
