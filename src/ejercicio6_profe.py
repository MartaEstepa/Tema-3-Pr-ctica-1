def calcula_precios(precio_normal, edades):
    res = []
    for edad in edades:
        if edad <= 18 or edad >= 65:
            #Precio reducido
            res.append(precio_normal//2)
        else: 
            #Precio normal
            res.append(precio_normal)
    return res

edades_personas = [8, 18, 25, 44, 64, 65, 70]
precios = calcula_precios(6, edades_personas)
print("El precio para cada persona es:", precios)
