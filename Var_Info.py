# Verificando as caracteristicas da variavel

v1 = input('Digite algo:')

# tipo primitivo da variavel
print('O tipo primitivo de v1 é:', type(v1))

# Só tem espaços?
print('Só tem espaços?', v1.isspace())
print('É um número?', v1.isnumeric())
print('É alfabético?', v1.isalpha() )
print('É alfanumérico?', v1.isalnum())
print('Está em maiusculas?', v1.isupper())
print('Está em minusculas?', v1.islower())
print('Está capitalizada?', v1.istitle())

