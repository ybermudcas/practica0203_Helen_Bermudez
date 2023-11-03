abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
abc = []

for i in range(len(abecedario)):
    if (i + 1) % 3 != 0:
        abc.append(abecedario[i])

       
print("Lista sin las posiciones múltiplo de 3:", abc)