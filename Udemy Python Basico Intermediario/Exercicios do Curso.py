print("\nFaça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.")
idade = int(input("Qual a sua idade? "))

if idade >= 18:
    print("Você é maior de idade!")
elif idade > 0 and idade < 18:
    print("Você ainda não é maior de idade!")
else:
    print("Idade incorreta")


print("\nFaça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = float((nota1+nota2)/2)

if media >= 6:
    print("Sua média é ", media, "Você foi Aprovado!")
else:
    print("Sua média é ", media, "Você foi Reprovado!")


print("\nEscreva um programa que resolva uma equação de segundo grau.")
#formula
    # a² + bx + c
    # (-b +- sqrt(b²-4ac))/2
import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

delta = (b**2) - 4 * a * c
raiz_delta = math.sqrt(delta)

x1 = (-b + raiz_delta)/(2*a)
x2 = (-b - raiz_delta)/(2*a)

print("x1 = ", x1)
print("x2 = ", x2)


print("\nEscreva um programa que ordene uma lista numérica com três elementos.")

import random
lista_ex4 = []
tam = 5
for i in range(tam):
    lista_ex4.append(random.randint(0, tam))
print(lista_ex4)  # modo automatico
# lista_ex4.sort()
for i in range(len(lista_ex4)):         # Modo manual
    menor = i

    for j in range(i+1, len(lista_ex4)):
        if lista_ex4[j] < lista_ex4[menor]:
            menor = j
    if lista_ex4[i] != lista_ex4[menor]:
        aux = lista_ex4[i]
        lista_ex4[i] = lista_ex4[menor]
        lista_ex4[menor] = aux

print(lista_ex4)


print("\nEscreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.\n")
# Calculadora 1
# def adicao(num_1, num_2):
#     return(num_1 + num_2)
#
# def multiplicar(num_1, num_2):
#     return(num_1 * num_2)
#
# def subtrair(num_1, num_2):
#     return(num_1 - num_2)
#
# def dividir(num_1, num_2):
#     return(num_1 / num_2)
#
# num_1 = float(input("Insira um numero: "))
# num_2 = float(input("Insira outro numero: "))
#
# operador = input("\nDigite o operador: \n '+' para somar \n '-' para subtrair \n '/' para dividir \n '*' para multiplicar \n")
#
# if operador == "+":
#     soma = adicao(num_1, num_2)
#     print(soma)
# elif operador == "-":
#     sub = subtrair(num_1, num_2)
#     print(sub)
# elif operador == "*":
#     mult = multiplicar(num_1, num_2)
#     print(mult)
# elif operador == "/":
#     try:
#         div = dividir(num_1, num_2)
#         print(div)
#     except ZeroDivisionError:
#         print("Divisão por 0 não é válida")
# else:
#     pass
# Calculadora 2
print("\nEscreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.\n")

# CALCULADORA PYTHON EXERCÍCIO DE FIXAÇÃO
# IDE PyCharm

# FUNÇÃO PARA REALIZAR ADIÇÃO
def soma(x, y):
    return x+y

# FUNÇÃO PARA REALIZAR SUBTRAÇÃO
def subtrair(x, y):
    return x-y

# FUNÇÃO PARA REALIZAR MULTIPLICAÇÃO
def multiplicar(x, y):
    return x*y

# FUNÇÃO PARA REALIZAR
def dividir(x, y):
    return x/y

# FUNÇÃO DO MENU
def menu():
    print("""
Selecione a operação desejada:
'+' para somar 
'-' para subtrair
'*' para multiplicar
'/' para dividir
'SAIR' para sair do programa
    """)
    return input("> ").upper()

# FUNÇÃO PARA CHECAR SE O USUÁRIO ESTÁ INSERINDO OS DADOS CORRETAMENTE
# SEM LETRAS OU OUTROS CARACTERES NO LUGAR DE NUMEROS INTEIROS OU DECIMAIS
def check_numeros():
    while True:
        try:
            return float(input("n > "))
        except ValueError:
            print("Por favor insira um número válido")
            continue

#LOOP CONTINUO ATÉ REALIZAR O COMANDO PARA SAIR DELE
while True:

    # operador = input("operacao > ").upper()
    operador = menu()               # CHAMA O MENU DE OPÇÕES

    if operador == "SAIR":          # COMANDO PARA SAIR DO LOOP
        print("saindo")             # E ENCERRAR O PROGRAMA
        break                       #

    elif operador == "+":
        # n1 = float(input("n1 > "))
        # n2 = float(input("n2 > "))
        n1 = check_numeros()
        n2 = check_numeros()
        print(f"{n1} + {n2} = {soma(n1, n2)}")

    elif operador == "-":
        # n1 = float(input("n1 > "))
        # n2 = float(input("n2 > "))
        n1 = check_numeros()
        n2 = check_numeros()
        print(f"{n1} - {n2} = {subtrair(n1, n2)}")

    elif operador == "*":
        # n1 = float(input("n1 > "))
        # n2 = float(input("n2 > "))
        n1 = check_numeros()
        n2 = check_numeros()
        print(f"{n1} * {n2} = {multiplicar(n1, n2)}")

    elif operador == "/":
        # n1 = float(input("n1 > "))
        # n2 = float(input("n2 > "))
        n1 = check_numeros()
        n2 = check_numeros()
        try:
            print(f"{n1} / {n2} = {dividir(n1, n2)}")
        except ZeroDivisionError:
            print("Divisão por 0 inválida")

    else:
        print("Comando inválido")

