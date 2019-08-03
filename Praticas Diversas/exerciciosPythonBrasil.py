# print("1- Faça um Programa que mostre a mensagem 'Alo mundo' na tela.\n")
# print("Alô mundo")

# print("\n2- Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].")
# n = input("Digite um numero: ")
# print("o numero informado é "+ n)

# print("\n3- Faça um Programa que peça dois números e imprima a soma.")
# a = int(input("Digite um numero "))
# b = int(input("Digite outro numero "))
# print("A soma de", a, "+", b, "é igual a ",a+b)

# print("\n4- Faça um Programa que peça as 4 notas bimestrais e mostre a média.")
# n1 = int(input("Nota 1: "))
# n2 = int(input("Nota 2: "))
# n3 = int(input("Nota 3: "))
# n4 = int(input("Nota 4: "))
# print("Sua Média é ", (n1+n2+n3+n4)/4)

# print("\n5- Faça um Programa que converta metros para centímetros.")
# mt = float(input("Digite o valor em metros a ser convertido: "))
# print(round(mt*100, 0))

# print("\n6- Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.")
# import math
# raio=int(input("Insira o valor do raio: "))
# dmt=float(raio*2)
# circ=float((math.pow(raio, 2)) * math.pi)
# print("o diametro é: ", dmt, "e a circunferência é de ", round(circ, 2))

# print("\n7- Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.")
# alt = float(input("digite a largura do quadrado: "))
# lar = float(input("digite a altura do quadrado: "))
# arq = float(alt*lar)
# print("a area é igual a", round(arq, 2), "e o dobro da area é de ", (round(arq, 2))*2)

# print("\n8- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.")
# gph = float(input("Quanto você ganha por hora? "))
# hrm = int(input("Quantas horas no mês você trabalhou? "))
# slm = float(gph*hrm)
# print("Seu salário nesse mês foi de $", round(slm,2))

# print("\n9- Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).")
# F = float(input("Grau em Fahrenheit (°F) "))
# C = float((5*(F-32)/9))
# print(round(F, 2),"°F = ", round(C,4),"°C")

# print("\n10- Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit. F=(C*(9/5))+32")
# C = float(input("Grau em Celsius (°C) "))
# F = float((C*(9/5))+32)
# print(round(C, 2), "°C = ", F, "°F")

# print("\n11- Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: \n\na.) o produto do dobro do primeiro com metade do segundo. \nb.) a soma do triplo do primeiro com o terceiro. \nc.) o terceiro elevado ao cubo.\n")
# import math
# ni1 = int(input("Digite um numero inteiro: "))
# ni2 = int(input("Digite um numero inteiro: "))
# nr1 = float(input("Digite um numero decimal: "))
# print("\na: ", (2*ni1)*(ni2/2),"\nb: ", (3*ni1)+nr1,"\nc: ", math.pow(nr1, 3))

# print("\n12- Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58\n")
# alt = float(input("Qual a sua altura(metros)?\n"))
# pid = (72.7 * alt)-58
# print("Seu peso ideal é de ", pid,"Kg")

# print("\n13- Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:\n Para homens: (72.7*h) - 58 \n Para mulheres: (62.1*h) - 44.7\n")
# h = float(input("Qual a sua altura(metros)?\n"))
# gen = input("Você é homem(M) ou mulher(F)?\n").upper()
#
# if gen == "F":
#     peso = (62.1 * h) - 44.7
#     print("Seu peso ideal é de ", peso, "Kg")
# elif gen == "M":
#     peso = (72.7 * h) - 58
#     print("Seu peso ideal é de ", peso, "Kg")
# else:
#     print("deu ruim")

# print("\n14- João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. \nToda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.\nJoão precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.\nImprima os dados do programa com as mensagens adequadas.\n")
# peso = float(input("Qual o peso da pescada(kg)?\n"))
# if peso > 50:
#     excesso = peso-50
#     multa = excesso * 4
#     print("Peso acima do limite em ",excesso,"Kg(s).", "Valor total pelo peso excedente é de R$", round(multa, 3))
# else:
#     print("Peso dentro do limite")

# print("\n15- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.\nCalcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:\na.)salário bruto.\nb.)quanto pagou ao INSS.\nc.)quanto pagou ao sindicato.\nd.)o salário líquido.\ne.)calcule os descontos e o salário líquido, conforme a tabela abaixo:\n+ Salário Bruto : R$\n- IR (11%) : R$\n- INSS (8%) : R$\n- Sindicato ( 5%) : R$\n= Salário Liquido : R$\nObs.: Salário Bruto - Descontos = Salário Líquido.\n")
# gph = float(input("Quanto você ganha por hora?\n"))
# hrm = int(input("Quantas horas você trabalhou nesse mês?\n"))
# sal_bruto = gph * hrm
# desc_ir = sal_bruto * .11
# desc_inss = sal_bruto * .08
# desc_sind = sal_bruto * .05
# sal_liq = sal_bruto - (desc_inss + desc_ir + desc_sind)
# print(f"""Planilha Salarial do mês:
# + Salário Bruto: R${sal_bruto}
# - IR (11%): R${desc_ir}
# - INSS (8%): R${desc_inss}
# - Sindicato (5%): R${desc_sind}
# = Salário Liquido: R${sal_liq}
# """)

# print("\n16- Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.\nConsidere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.\nInforme ao usuário a quantidades de latas de tinta a serem compradas e o preço total.\n")
# import math
# mts_2 = float(input("Quantidade em m² para ser pintada: "))
# lts_tinta = mts_2 / 3     # Tinta necessária
# lata_valor = 80
# lts_lata = 18
# lata_qtd = math.ceil(lts_tinta / lts_lata)
# valor_total = lata_qtd * lata_valor
# print(lata_qtd, valor_total)
# print(f"Quantidade necessária de latas: {lata_qtd}, totalizando R${round(valor_total, 2)}")

# print("""
# 17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.\n""")
# import math
# mts_2 = float(input("Quantidade em m² a ser pintada: "))
# lts_mt2 = mts_2 / 6     # Tinta necessária
#
# lata_preco = 80
# lata_lts = 18
# galao = 3.6
# galao_preco = 25
#
# lts_tot = math.ceil(float(lts_mt2 * 1.1))                       # Qtd de litros
# latas_qtd = math.ceil(float(lts_tot / 18))                      # Qtd de Latas
# galoes_tot = math.ceil(float(lts_tot) / float(galao))           # Qtde de galoes
# latas_vl = latas_qtd * lata_preco                               # Valor da lata
# galoes_vl = galoes_tot * galao_preco                            # Valor de galoes
#
# # mistura
# m1 = int(lts_tot / 18) # Latas
# m2 = lts_tot % 18
# m3 = math.ceil(m2 / galao) # Galoes
# m4 = (m1 * lata_preco) + (m3 * galao_preco)
#
#
# print(f"Quantidade de tinta {lts_tot} litros")
# print(f"Quantidade em latas {latas_qtd}(latas) no valor de R$ {latas_vl}")
# print(f"Quantidade em galoes {galoes_tot}(galões) no valor de R$ {galoes_vl}")
# print(f"Galoes {m3}(galões) e latas {m1}(latas) misturados no valor de R$ {m4}")

print("18- Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).\n")
file_size = float(input("Tamanho (em MB) do arquivo para download: "))
net_spd = float(input("Velocidade do link de Internet (em Mbps): "))

taxa_download = net_spd / 8
tempo_download = (file_size / taxa_download) / 60

print(f"""
Velocidade aproximada de download é de {taxa_download} MBps
Tempo aproximado para concluir o download é de {round(tempo_download, 1)} minutos
""")



