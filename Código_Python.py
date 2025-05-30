# calculadora simples com Python
op = ''
while op != 's' :
op =  input
num1 = float(input(" Digite o primeiro número: "))
num2 = float(input(" Digite o segundo número: "))

# Calculando a soma e armazenando na variável 'soma'
soma =  num1 + num2

# Calculando a subtração e armazenando na variável 'subtração'
subtracao = num1 - num2

# Calculando a multiplicação e armazenando na variável ' multiplicação'
multiplicacao = num1 * num2

# Calculando a divisão e armazenando na variável ' divisão'
divisao = num1 / num2

# Calculando a exponenciação e armazenando na variável 'expo'
expo = num1 ** num2

# Calculando o resto da divisão e armazenando na variável 'resto'
resto = num1 % num2
# Impressão dos resultados
print('Soma :                ', num1, '+',num2, '=', soma)
print('Subtracao :           ', num1, '-', num2, '=', subtracao)
print('Multiplicacao :       ', num1, '*', num2, '=', multiplicacao)
print('Divisao :             ', num1, '/', num2, '=', divisao)
# Impressão dos resultados
print('Soma :                ', num1, '+',num2, '=', soma)
print('Subtracao :           ', num1, '-', num2, '=', subtracao)
print('Multiplicacao :       ', num1, '*', num2, '=', multiplicacao)
print('Divisao :             ', num1, '/', num2, '=', divisao)
print('Expo :                ', num1, '**', num2, '=', expo)
print('Resto :               ', num1, '%', num2, '=', resto)
#else:
#  resultado = 'Operação não suportada'
#  print("O resultado da operação é: " + str(resultado))

