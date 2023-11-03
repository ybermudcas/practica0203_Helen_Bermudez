asignaturas = ["Matemáticas", "Física", "Química", "Lengua"]
repetir = []

for asignatura in asignaturas:
    nota = float(input("Introduce la nota para " + asignatura + ": "))
    if nota < 5.0:
        repetir.append(asignatura)

print("Debes repetir las siguientes asignaturas:")
for asignatura in repetir:
      print(asignatura)
    