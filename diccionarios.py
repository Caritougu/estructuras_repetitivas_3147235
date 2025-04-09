#Diccionario 
#Es una coleccion de datos que 
# los almacena en pares 
# clave valor 
# un diccionario comienza y 
# termina con llaves (curly braces)
# la clave es un string 
# pero el valor puede ser de cualquier tipo 
# la clave se separa del valor 
# por dos puntos (:) 
# y lo mismo cada elemento y propiedad del diccionario 
# se separa por una coma

#EJEMPLO:diccionario 
#que almacene los datos de un 
#pais 
pais1 = {
    "nombre": "Argentina",
    "capital": "Buenos Aires",  # Corregí la ortografía de "Buenos Aires"
    "moneda": "Peso argentino",
    "ciudades": [
        "Córdoba",
        "Rosario",
        "Mendoza"
    ],
    "poblacion": {
        "censo": 45,  
        "densidad": 17  
    }
}
  
    
     

pais2 = {
    "nombre": "Ecuador",
    "capital": "Quito",
    "moneda": "Dólar",
    "ciudades": [
        "Guayaquil",
        "Durán",
        "Portoviejo"
    ],
    "poblacion": {
        "censo": 18,
        "densidad": 64 
    }
}

                        
    
        
pais3 = {
    "nombre": "Paraguay",
    "capital": "Asunción",
    "moneda": "Guaraní",
    "ciudades": [
        "San Lorenzo",
        "Lambaré",
        "Luque"
    ],
    "poblacion": {
        "censo": 46,
        "densidad": 18
    }
}

#Acceder a la informacion del pais 
print(pais1["moneda"])
print(pais1["capital"])
#Acceder a una ciudad
print(pais1["ciudades"][1])
print("..............")
#Iterar las ciudades del pais1 con un for 
for ciudad in pais1["ciudades"]:
    print(ciudad)
#Acceder a datos poblacionales
print("..............")
print("Censo:",
      pais1["poblacion"]["censo"],
      "en millones de habitantes")

print("Densidad:",
      pais1["poblacion"]["densidad"],
      "por metro cuadrado")
