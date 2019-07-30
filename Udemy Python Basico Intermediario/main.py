import aleatorio as a
import media as m

lista = a.geraListaInteiro(4)
print(lista)

media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)

print("A média da minha lista é "+str(media))
print("A mediana da minha lista é "+str(mediana))
print("A moda da minha lista é "+str(moda))

