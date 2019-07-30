# print("Hello World")
# print("teste olá")
# print(10%3) #modulo retorna o resto da divisao
# x=1
# y=2
# if x == y:
#     print("numeros iguais")
# elif x < y:                     #elif faz com que se execute a primeira condição verdadeira que encontrar
#     print("x menor que y")
# elif y > x:
#     print("y maior que x")
# else:
#     print("numeros diferentes")

# x=1
# while x<10:
#     print(x)
#     x+=1

# lista1 = [1,2,3,4,5]
# lista2 = ["ola", "mundo", "!"]
# lista3 = [0, "ola", "biscoito", "bolacha", 99.9]

# for i in lista3:
#     print(i)

# for i in range(0, 22, 2): # range (0,22,2) parte do 0 até o 22 de 2 em 2 numeros - taboada do 2
#     print(i)

# a = "Diego"
# b = "Mariano"
# concatenar = a + " " + b + "\n"
# tamanho = len(concatenar) #conta a quantidade total de caracteres da string, incluindo espaçoes
# print(concatenar)
# print(tamanho)
# print(concatenar[0:3]) #imprime do valor 0(primeira letra) até o valor 3(terceira letra)
# print(concatenar.lower()) #converte os caracteres para minusculo
# print(concatenar.upper()) #converte os caracteres para maiusculo
# print(concatenar.strip()) #remove espaços e caracteres especiais

# minha_string = "O rato roeu a roupa do rei de Roma"
# minha_lista = minha_string.split() #separa/quebra a string
# print(minha_lista)
# minha_lista = minha_string.split("r") #separa a string e retira o r dela, case sensitive
# print(minha_lista)
# busca = minha_string.find("rei") #encontra a posição que a palavra está na string
# print(busca)
# print(minha_string[busca:]) #imprime a partir da palavra encontrada
# minha_string = minha_string.replace("o rei", "a rainha") #substitui a palavra na string
# print(minha_string)


# def soma(x, y):           # funcao de somar
#     return(x+y)             

# def multiplicacao(x, y):  # funcao de multiplicar              
#     return(x*y)

# s = soma(2, 3)            #retorna o valor da funcao "soma" para a variavel "s"
# m = multiplicacao(3, 4)   #retorna o valor da funcao "multiplicacao" para a variavel "m"

# print(s, m)
# print(soma(s, m))  #realiza a funcao soma com o resultado das operacoes

# arquivo_teste = open("arquivo_teste.txt")
# linhas = arquivo_teste.readlines()   # lê as linhas do arquivo
# print(linhas)                        # imprime as linhas do arquivo em uma lista
# for linhas in linhas:                # imprime linha por linha do arquivo
#     print(linhas)
# texto_completo = arquivo_teste.read()  # lê o arquivo inteiro
# print(texto_completo)                  # imprime o arquivo inteiro

# w = open("arquivo_teste2.txt", "w")     # cria um arquivo em branco

# w.write("Esse é o meu arquivo")    # Grava conteúdo ao arquivo | "w" subscreve
# w.close()                          # Fecha o arquivo após gravar !IMPORTANTE FECHAR O ARQUIVO APÓS GRAVAR

# w = open("arquivo_teste2.txt", "a")  # "a" atualiza o arquivo

# w.write("\nEssa é uma nova informação no arquivo")
# w.close()

# minha_lista = ["abacaxi", "melância", "abacate"]
# minha_lista_2 = [1,2,3,4,5]
# minha_lista_3 = ["abacaxi", 2, 9.89, True]

# print(minha_lista[2]) # imprime a posição 2 da lista (lista começa com indice 0)

# for item in minha_lista: # imprime todos os itens da lista
#     print(item)

# tamanho = len(minha_lista)  # checa o tamanho da lista, quantos itens a lista possui
# print(tamanho)

# minha_lista.append("limonada")  # insere a string "limão" na lista
# minha_lista.append("limoeiro")
# print(minha_lista)

# if 7 in minha_lista_2:
#     print("5 Está na lista")
# else:
#     print("Não está na lista")

# del minha_lista[2:] # remove a partir do item 2 até o ultimo item da lista 
# print(minha_lista)  # ou até definir um valor [2:4], aqui é o quarto item ou [:] apagar toda lista

# minha_lista_4 = []          # cria uma lista em branco
# minha_lista_4.append(57)    # e adiciona um item novo à ela através do "append()""

# print(minha_lista_4)

# lista = [124, 345, 5, 72, 46, 6, 7, 3, 1, 7, 0]
# print("Lista original:\n", lista)
# lista.sort()    # apenas altera a lista original, não retorna um valor
# print("Lista Ordenada numericamente:\n", lista)
# lista = sorted(lista)
# print("Lista Ordenada numericamente usando 'sorted()':\n", lista) # metodo que retorna um valor
# lista.sort(reverse=True)    # método usado para ordenar os valores da lista de forma decrescente
# print("Lista Ordenada numericamente decrescente:\n", lista)
# lista.reverse()     # método usado para reverter a lista
# print("Lista Revertida: \n", lista)

# lista2 = ["bola", "abacate", "dinheiro"]            # O mesmo serve para listas com string
# print("\nLista Original:\n", lista2)                # Podem ser ordenadas alfabeticamentes
# lista2.sort(reverse=True)                           # em ordem crescente ou decrescente
# print("Lista ordenada alfabeticamente:\n", lista2)  # 

# dicionario_sites = {"Diego": "diegomariano.com", "Google": "google.com.br", "Udemy": "udemy.com"}
#                         # Diego é uma chave para diegomariano.com
# # print(dicionario_sites['Diego'])  # imprime o elemento que está sendo chamado
# for chaves in dicionario_sites:     # Usa um laço para imprimir vários elementos do
#     print(dicionario_sites[chaves]) # dicionário

# import random
# # random.seed(1) # Força sempre o mesmo resultado
# # numero = random.randint(0,10) # Seleciona um numero aleatório dentro da margem especificada
# lista = [6, 45, 9]
# numero = random.choice(lista) # escolhe aleatoriamente um numero da lista
# print(numero)

# a = 2
# b = 0
# try:
#     print(a/b)                              # Testa condições que poderiam interromper 
# except:                                     # a execução do resto do código
#     print("Não é permitida divisão por 0")
# print(a/a)

