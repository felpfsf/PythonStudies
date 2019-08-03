# CALCULADORA PYTHON EXERCÍCIO DE FIXAÇÃO
# UMA DAS MUITAS FORMAS DE PROGRAMAR UMA CALCULADORA BÁSICA
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


# INICIO DO PROGRAMA
# LOOP CONTINUO ATÉ REALIZAR O COMANDO PARA SAIR DELE

loop = 1               # INICIA A VARIÁVEL COM O VALOR 1
while loop:            # INICIA E MANTÉM O LOOP ENQUANTO A VARIÁVEL "loop" FOR IGUAL A 1

    # operador = input("operacao > ").upper()
    operador = menu()               # CHAMA O MENU DE OPÇÕES

    if operador == "SAIR":          # CHECA O COMANDO DIGITADO PARA FINALIZAR O LOOP
        loop = 0                    # FINALIZA O LOOP APLICANDO O VALOR 0 À VARIÁVEL "loop"

    elif operador == "+":
        n1 = check_numeros()
        n2 = check_numeros()
        print(f"{n1} + {n2} = {soma(n1, n2)}")

    elif operador == "-":
        n1 = check_numeros()
        n2 = check_numeros()
        print(f"{n1} - {n2} = {subtrair(n1, n2)}")

    elif operador == "*":
        n1 = check_numeros()
        n2 = check_numeros()
        print(f"{n1} * {n2} = {multiplicar(n1, n2)}")

    elif operador == "/":
        n1 = check_numeros()
        n2 = check_numeros()
        try:
            print(f"{n1} / {n2} = {dividir(n1, n2)}")
        except ZeroDivisionError:
            print("Divisão por 0 inválida")

    else:
        print("Comando inválido")

print("Obrigado por usar a calculadora")        # IMPRIME UMA MENSAGEM AO TERMINAR O PROGRAMA.
