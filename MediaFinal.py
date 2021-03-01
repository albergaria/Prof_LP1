# Exercio 01
# Calculo da media final de um aluno

# Calcular a media final de um determinado aluno com base nas notas das 3 provas que ele fez.
# Se a media for maior que 6 ele é aprovado. Caso contrario reprovado.

#Passo a passo

# 1 - Perguntar o nome do aluno
# 2 - Perguntar a nota da prova 1
# 3 - Perguntar a nota da prova 2
# 4 - Perguntar a nota da prova 3
# 5 - Calcular a media das 3 provas
# 6 - Verificar se o aluno foi aprovado ou reprovado
# ----------------------------------------------------------
print(' Calculo da média final do aluno')
print()
Nome = input('Nome do aluno:')

# str() - Texto
# int() - Numero inteiro. Sem casa decimal
# float() - Numero com casa decimal
Nota1 = float(input('Nota da prova 1:'))
Nota2 = float(input('Nota da prova 2:'))
Nota3 = float(input('Nota da prova 3:'))
Media = (Nota1+Nota2+Nota3)/3
print('A média final do aluno', Nome, ' é:',Media)

if (Media > 6):
    print('O aluno foi APROVADO')
else:
    print('O aluno foi REPROVADO')
