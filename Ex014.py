# Escreva um programa que converta uma temperatura digitada em °C para °F
# Regra de conversao: (( 9 x temp em celcius ) / 5 ) + 32

tc = float(input('Informe a temperatura em °C:'))
tf = ((9 * tc) / 5) + 32
print('A temperatura em {}°C é igual a {}°F!'.format(tc, tf))
