# Exercicio 01
# Escrever um programa que leia um numero inteiro e mostre na tela o seu successor e seu antecessor.

numero = int(input('Informe um numero:'))
antecessor = numero - 1
sucessor = numero + 1

print('O numero informado foi {}. O seu antecessor é {} e o seu sucessor é {}'.format(numero, antecessor, sucessor))

print('O numero informado foi {}'.format(numero))
print('O seu antecessor é {}'.format(antecessor))
print('O seu sucessor é {}'.format(sucessor))

# ------------------------------------------------------------------------
# Exercicio 02
# Escrever um programa que leia um numero e mostre o seu dobro, o triplo e a raiz quadrada.

numero = float(input('Digite um numero:'))
dobro = numero * 2
triplo = numero * 3
raizq = numero**(1/2)
print('O numero é {}. O dobro é {:.1f}, o triplo é {:.2f} e a raiz quadrada é {:.3f}'.format(numero, dobro, triplo, raizq))

# ------------------------------------------------------------------------
# Exercicio 03
# Escrever um programa que leia duas notas de um aluno e calcule e mostre a sua media.

nome = input('Informe o nome do aluno:')
nota1 = float(input('Informe a nota 1:'))
nota2 = float(input('Informe a nota 2:'))

soma = (nota1 + nota2)
media = soma / 2
print('A média das notas é {:.1f}'.format(media))
