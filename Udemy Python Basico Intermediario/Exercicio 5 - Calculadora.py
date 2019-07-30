def soma(x, y):
    return x+y

def subtrair(x, y):
    return x-y

def multiplicar(x, y):
    return x*y

def divisao(x, y):
    return x/y


while True:
    print("""
    Bem vindo a calcPy 1
    
    '+' para somar
    '-' para subtrair
    '*' para multiplicar
    '/' para dividir
    """)

    operador = input("> ").upper()

    if operador == "SAIR":
        print("Obrigado por usar a calcPy 1")
        break

    # elif operador != str:
    #     print("Comando inválido")

    else:

        num_1 = float(input("Digite o primeiro valor: "))
        num_2 = float(input("Digite o segundo valor: "))

        if operador == "+":
            ad = soma(num_1, num_2)
            print(f"{num_1} + {num_2} = {ad}")

        elif operador == "-":
            sub = subtrair(num_1, num_2)
            print(f"{num_1} - {num_2} = {sub}")

        elif operador == "*":
            multi = multiplicar(num_1, num_2)
            print(f"{num_1} x {num_2} = {multi}")

        elif operador == "/":
            try:
                div = divisao(num_1, num_2)
                print(f"{num_1} / {num_2} = {div}")
            except ZeroDivisionError:
                print("Divisão inválida")

        else:
            print("Comando inválido")
