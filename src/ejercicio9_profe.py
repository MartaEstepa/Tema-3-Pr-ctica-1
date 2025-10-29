from collections import namedtuple

Persona = namedtuple("Persona", "nombre, edad")

def lee_personas(n):
    res = []
    for i in range(n): # 0, 1, 2, ..., n-1
        nombre = input(f"Nombre de la persona{i+1}: ")
        edad = int(input(f"Edad de la persona {i+1}: "))
        res.append(Persona(nombre,edad))
    return res


def edad_media(media):
    '''
    Función edad_media, que recibe una lista de personas y devuelva la edad media.
    '''
    #Esquema de SUMA
    if len(personas) == 0: #Para evitar luego división por cero
        return None #Si la lista está vacía, la media no está definida
    
    else:
        suma = 0
        for p in personas:
            suma += p.edad
        
        return suma/len(personas)


def mayores_18(personas):
    '''
    Función mayores_18, que recibe una lista de personas y devuelva una lista ordenada alfabéticamente con los nombres de las personas mayores de edad.
    '''
    mayor_edad = []
    for p in personas:
        if p.edad >= 18:
            mayor_edad.append(p.nombre)
    
    #Opción 1:sort ordena 'in_place'
    mayor_edad.sort()
    return mayor_edad

    #Opción 2: sprted devuelve una nueva lista ordenada
    return sorted(mayor_edad)


def edades_distintas(personas):
    '''
    Función edades_distintas, que recibe una lista de personas y devuelva una lista con las edades ordenadas de menor a mayor y sin duplicados.
    '''
    edades = set() #NO es un conjunto vacío, sino que es un diccionario
    for p in personas:
        edades.add(p.edad)
    #sorted siempre 
    #independientemente de lo que reciba
    return sorted(edades)


def persona_mas_joven(personas):
    '''
    Función persona_mas_joven, que reciba una lista de personas y devuelva el nombre de la persona de menor edad.
    '''
    '''
    menor = []
    mas_pequeño = 100
    for p in personas:
        if p.edad < mas_pequeño:
            mas_pequeño = p.edad
    return mas_pequeño
    '''
    persona_menor = None
    for p in personas:
        if persona_menor == None or p.edad < persona_menor.edad:
            persona_menor = p
    return persona_menor.nombre

n = 3
personas = lee_personas(n)
print(personas)
print("Edad Media: ", edad_media(personas))
print("Mayores de edad: ", mayores_18(personas))
print("Edades distintas: ", edades_distintas(personas))
print("Persona más joven: ", persona_mas_joven(personas))
