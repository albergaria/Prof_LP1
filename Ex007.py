# Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua média

n1 = float(input('Informe a nota 1 do aluno:'))
n2 = float(input('Informe a nota 2 do aluno:'))
m = (n1 + n2)/2
print('A média das notas do aluno é: {:.2f}'.format(m))