# media, mediana, moda
from statistics import *

def media(lista):
    #return mean(lista) # método fácil com uso de statistics
    media = sum(lista)/float(len(lista))  # soma todos os itens da lista e divide 
                                          # e divide pela quantidade total de itens
    return media

def mediana(lista):
    # return median(lista)  # método fácil
    lista_ordenada = sorted(lista)
    t = len(lista_ordenada)

    if t % 2 == 0:
        mediana = (lista_ordenada[int(t/2)]+lista_ordenada[int((t/2)-1)])/2
    elif t % 2 == 1:
        mediana = lista_ordenada[int((t/2))]

    return mediana

def moda(lista):
    # return mode(lista) # método fácil
    lista_dic = {}

    for l in lista:                      #  Conta todos os elementos da lista  
        if l not in lista_dic:           # 
            lista_dic[l] = 1             # 
        else:                            # 
            lista_dic[l] += 1            # 

    maior_repeticao = max(lista_dic.values())  # método values() retorna todos os valores da lista

    for i in lista_dic:
        if lista_dic[i] == maior_repeticao:
            moda = i

    return moda
