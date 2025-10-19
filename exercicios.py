# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
soma = numero1 + numero2
print("A soma dos dois números inteiros é:", soma)


# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
resto = numero1 % numero2
print("O resto da divisão é:", resto)


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
multiplicacao = numero1 + numero2
print("A multiplicação dos dois números inteiros é:", multiplicacao)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
divisao = numero1 // numero2
print("A divisão dos dois números inteiros é:", divisao)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero = int(input("Digite um número inteiro: "))
quadrado = numero ** 2
print("O quadrado do número é:", quadrado)


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
numero1 = float(input("Digite o primeiro número flutuante: "))
numero2 = float(input("Digite o segundo número flutuante: "))   
soma = numero1 + numero2
print("A soma dos dois números flutuantes é:", soma)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero1 = float(input("Digite o primeiro número flutuante: "))
numero2 = float(input("Digite o segundo número flutuante: "))       
media = (numero1 + numero2) / 2
print("A média dos dois números flutuantes é:", media)

# 7.1 Crie um programa que calcule a média de números flutuantes fornecidos pelo usuário. O programa deve calcular a média de acordo com o numero de valores inseridos que pode ser ate 10 elementos.

numeros = []

for i in range(10):
    entrada = input(f"Digite o número flutuante {i+1} (ou digite 'sair' para finalizar): ")

    if entrada.strip().lower() == 'sair':
        break

    try:
        # aceita vírgula como separador decimal também
        numero = float(entrada.replace(',', '.'))
    except ValueError:
        print("Valor inválido. Tente novamente.")
        continue

    numeros.append(numero)

if len(numeros) > 0:
    media = sum(numeros) / len(numeros)
    print("A média dos números flutuantes é:", media)
else:
    print("Nenhum número foi inserido.")




# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite a base (número flutuante): "))
expoente = float(input("Digite o expoente (número flutuante): "))
potencia = base ** expoente
print("O resultado da potência é:", potencia)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32   
print("A temperatura em Fahrenheit é:", fahrenheit)


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# Formatando a saída com duas casas decimais
import math
raio = float(input("Digite o raio do círculo: "))           
area = math.pi * (raio ** 2)
print(f"A área do círculo é: {area:.2f}")


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
texto1  = input("Digite uma texto: ")
texto_maiusculas = texto1.upper()
print("A texto em maiúsculas é:", texto_maiusculas)


# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nomecompleto  = input("Digite seu nome completo: ")
nome_minusculas = nomecompleto.lower()
print("Seu nome em minúsculas é:", nome_minusculas)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase  = input("Digite uma frase: ")
frase_sem_espacos = frase.strip()   
print("A frase sem espaços em branco no início e no final é:", frase_sem_espacos)


# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data1 = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data1.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)

#14.1 Faça um programa que peça ao usuário para digitar uma data no formato "dd-mm-aaaa" e, em seguida, imprima o dia, o mês e o ano em formato de lista.
data1 = input("Digite uma data no formato dd-mm-aaaa: ")
lista = data1.split("-")
print(lista)


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
string_concatenada = string1 + string2
print("A string concatenada é:", string_concatenada)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
expressao1 = input("Digite a primeira expressão booleana (True/False): ")
expressao2 = input("Digite a segunda expressão booleana (True/False): ")
bool1 = expressao1.strip().lower() == 'true'
bool2 = expressao2.strip().lower() == 'true'
resultado_and = bool1 and bool2
print("O resultado da operação AND é:", resultado_and)


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
expressao1 = input("Digite a primeira expressão booleana (True/False): ")
expressao2 = input("Digite a segunda expressão booleana (True/False): ")
bool1 = expressao1.strip().lower() == 'true'
bool2 = expressao2.strip().lower() == 'true'
resultado_and = bool1 or bool2
print("O resultado da operação OR é:", resultado_and)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
expressao1 = input("Digite uma expressão booleana (True/False): ")
bool1 = expressao1.strip().lower() == 'true'    
resultado_invertido = not bool1
print("O valor invertido é:", resultado_invertido)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
sao_iguais = numero1 == numero2
print("Os dois números são iguais?", sao_iguais)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
sao_diferentes = numero1 != numero2
print("Os dois números são diferentes?", sao_diferentes)

# #### try-except e if


# 21: Conversor de Temperatura
temperature_celsius = input("Digite a temperatura em Celsius: ")
try:
    celsius = float(temperature_celsius)
    fahrenheit = (celsius * 9/5) + 32
    print("A temperatura em Fahrenheit é:", fahrenheit)
except ValueError:
    print("Valor inválido. Por favor, insira um número válido para a temperatura.")


# 22: Verificador de Palíndromo
frase = input("Digite uma frase: ")
frase_limpa = ''.join(frase.split()).lower()
if frase_limpa == frase_limpa[::-1]:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")


# 23: Calculadora Simples
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
operacao = input("Digite a operação (+, -, *, /): ")
try:
    numero1 = float(num1)
    numero2 = float(num2)
    
    if operacao == '+':
        resultado = numero1 + numero2
    elif operacao == '-':
        resultado = numero1 - numero2
    elif operacao == '*':
        resultado = numero1 * numero2
    elif operacao == '/':
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            print("Erro: Divisão por zero não é permitida.")
            resultado = None
    else:
        print("Operação inválida.")
        resultado = None

    if resultado is not None:
        print("O resultado da operação é:", resultado)
except ValueError:
    print("Valor inválido. Por favor, insira números válidos.")




# 24: Classificador de Números
num1 = input("Digite um número: ")
try:
    numero = float(num1)
    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")
except ValueError:
    print("Valor inválido. Por favor, insira um número válido.")



# 25: Conversão de Tipo com Validação
valor = input("Digite um valor numérico: ")
try:
    numero = float(valor)
    print("O valor convertido para float é:", numero)   
except ValueError:
    print("Valor inválido. Por favor, insira um número válido.")


# 26: Is isntance Check para Inteiro
valor = input("Digite um valor: ")
try:
    numero = float(valor)
    if isinstance(numero, int):
        print("O valor é do tipo ine.")
    else:
        print("O valor não é do tipo int.")
except ValueError:
    print("Valor inválido. Por favor, insira um número válido.")


# 27: Is isntance Check para dataframe do pandas
import pandas as pd
valor = input("Digite um valor: ")

try:    
    df = pd.DataFrame([float(valor)])
    if isinstance(df, pd.DataFrame):
        print("O valor é do tipo DataFrame do pandas.")
    else:
        print("O valor não é do tipo DataFrame do pandas.")
except ValueError:
    print("Valor inválido. Por favor, insira um número válido.")    