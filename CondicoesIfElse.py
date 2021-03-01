# Condição - if

idade = int(input('Informe sua idade: '))

if idade >= 18:
    print('Você já um adulto!')
print('Fim od programa!')


# Condição - if e else

idade = int(input('Informe sua idade: '))

if idade >= 18:
    print('Você já um adulto!')
else:
    print('Você ainda é menor de idade!')


# Condicao - if - elif - else
idade = int(input('Informe sua idade: '))

if idade < 12:
    print('crianca')
elif idade < 18:
    print('adolescente')
elif idade < 60:
    print('adulto')
else:
    print('idoso')






'''
# if
idade = 18
if idade < 20:
    print('Você é jovem!')

# if ... else
idade = 18
if idade >= 18:
    print('maior de idade')
else:
    print('menor de idade')

# if ... elif ... else
idade = 18
if idade < 12:
    print('crianca')
elif idade < 18:
    print('adolescente')
elif idade < 60:
    print('adulto')
else:
    print('idoso')

'''