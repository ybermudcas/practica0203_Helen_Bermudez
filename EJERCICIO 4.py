numeros_ganadores = []

while True:
    numero = input("Ingresa un número ganador o escribe 'listo' cuando hayas introducido todos ")
    
    numeros_ganadores.append(numero)
    
    if numero.lower() == "listo":
       break
    
numeros_ganadores.sort()
    
print(numeros_ganadores)