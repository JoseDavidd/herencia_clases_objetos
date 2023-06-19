from alumno import Alumno
from aula import Aula
from profesor import Profesor

aulas =[
    Aula(Profesor("Manolo Gutierrez", 0, 9)),
    Aula(Profesor("Fernando Sanchez", 3, 6)),
    Aula(Profesor("Paula Tejero", 2, 7)),
    Aula(Profesor("Alicia Pomares", 1, 8)),
    Aula(Profesor("Alejandro SantaMaria", 2, 10))
]

CANTIDAD = {
    "alumnos" : 5
}

aulas[0].add(Alumno("PEPITO", "A", "PEPI@TO.com"))

for i in range(CANTIDAD["alumnos"]):
    aulas[i % len(aulas)].add(Alumno())
contador = 0


for aula in range(len(aulas)):
    try:
        aulas[contador].puntuar()
        aulas[contador].convocar_examen()
        contador += 1
    except Exception as e:
        print(e)
