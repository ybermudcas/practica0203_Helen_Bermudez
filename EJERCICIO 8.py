palabra =input("Escribe una palabra para saber si es palíndroma")
palabra_lista = list(palabra)
reversa = palabra_lista[::-1]


if palabra_lista == reversa:
    print(palabra, "es una palabra palindroma")

else:
    print(palabra, "no es una palabra palíndroma")


#palabra_inver = palabra_lista.reverse()

#if palabra == palabra_inver:
 #   print("Es una palabra palíndroma")

#else:
 #   "No es una palabra palíndroma"
