
asignaturas = ["Matemática", "Biología", "Lengua", "Física"]
notas = []

for asignatura in asignaturas:
    nota = float(input("¿Qué nota sacaste en " + asignatura + "? "))
    notas.append(nota)

for i in range(len(asignaturas)):
    print("En", asignaturas[i], "has sacado", notas[i])