# Laboratorio N°2.2
# Ejercicio 3
# Elaborado por Sergio Jesús Miguel Herrera del Carpio

# Parte a 
lista = [('Jose', 1988), ('Marta', 2005), ('Piero', 2015), ('Luisa', 2000)]
mayor = lista[0]
for persona in lista:
    if persona[1] < mayor[1]:
        mayor = persona
print("La persona de mayor edad es", mayor[0])

# Parte b
N = int(input("Ingrese el año: "))
personasM = []
for persona in lista:
    if persona[1] < N:
        personasM.append(persona[0])
personasmenores= " ". join(personasM)
print("Los nombres antes del año ",N," son: ",personasmenores)
