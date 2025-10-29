from collections import namedtuple
import csv
from datetime import datetime

Libro = namedtuple("Libro", "isbn,titulo,autor,fecha_publicacion,precio,disponible")


def lee_libros(ruta_csv):
    with open(ruta_csv, encoding="utf-8") as f:
        res = []
        lector = csv.reader(f)
        next(lector)
        for isbn, titulo, autor, fecha_publicacion, precio, disponible in lector:
            fecha_publicacion = datetime.strptime(fecha_publicacion, "%d/%m/%Y").date()
            precio = float(precio)
            disponible = disponible == "Sí"
            res.append(
                Libro(isbn, titulo, autor, fecha_publicacion, precio, disponible)
            )
        return res


# TODO: Implemente las funciones solicitadas en el enunciado
def autores_disponibles(libros, inicial):
    '''
    devuelve una lista ordenada alfabéticamente con los nombres
    de los autores cuya inicial es la indicada y para los que hay
    libros en stock en la librería.
    La lista no puede contener duplicados
    '''

    autores = set()
    for libro in libros:
        # Hay un método en str llamado startwith (empieza con)
        if libro.autor[0] == inicial and libro.disponible:
            autores.add(libro.autor)
        return sorted(autores)


def titulos_baratos_actuales(libros):
    '''
    devuelve una lista con los títulos de los libros con un precio
    inferior a 20 euros que hayan sido publicados a partir del año 2001
    '''
    titulos = []
    for libro in libros:
        if libro.precio < 20 and libro.fecha_publicacion.year >= 2001:
            titulos.append(libro.titulo)
    return titulos


def media_precios(libros, palabra):
    '''
    devuelve la media del precio de los libros que contienen en su
    título la palabra en cuestión. Si no se encuentra ningún libro
    con dicha palabra en el titulo, la funcion devulve None.
    NOTA: La búsqueda de los libros con la palabra en el título
    no debe ser sensible a mayúsculas.
    '''
    suma = 0
    contador = 0 # Necesito contar los libros para calcular la media
    palabra = palabra.lower() #para no tener que recalcularlo en cada iteación
    for libro in libros:
        if palabra in libro.titulo.lower():
            suma += libro.precio
            contador += 1
    if contador == 0:
        return None
    return suma / contador # Esto solo se ejecuta si contador != 0



def libro_mas_reciente(libros):
    '''
    devuelve el libro con la fecha de publicación más reciente
    '''
    libro_mas_reciente = None
    for libro in libros:
        if libro_mas_reciente == None or \
        libro.fecha_publicacion > libro_mas_reciente.fecha_publicacion:
            libro_mas_reciente = libro
    return libro_mas_reciente


if __name__ == "__main__":
    libros = lee_libros("data/libreria.csv")
    print(f"Se han leído {len(libros)} libros.")

    print("Autores disponibles:", autores_disponibles(libros, "M"))
    print("Titulos baratos actuales:", titulos_baratos_actuales(libros))
    print(
        "Media de precios de libros con la palabra 'El':", media_precios(libros, "El")
    )
    print("Libro más reciente:", libro_mas_reciente(libros))
