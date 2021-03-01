# Faça um programa que leia a largura e a altura da parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m2

largura = float(input('Informe a largura da parede em metros:'))
altura = float(input('Informe a altura da parade em metros:'))
area = largura * altura
print('A sua parede de {} x {} tem uma area de {:.2f} m2. \n Serão necessários {:.2f} litros de tinta para a pintura.'.format(largura, altura, area, (area/2)))
