
paises = [
    {
        "nombre": "Venezuela",
        "capital": "Caracas",
        "moneda": "Bolívar",
        "poblacion": {
            "censo": 31,  # Población en millones
            "densidad": 26  # Densidad poblacional
        },
        "ciudades": [
            "Caracas",
            "Maracaibo",
            "Valencia",
            "Carabobo"
        ],
        "superficie": 916445  # Superficie en km²
    },
    {
        "nombre": "Brasil",
        "capital": "Brasilia",
        "moneda": "Real",
        "poblacion": {
            "censo": 213,  # Población en millones
            "densidad": 25  # Densidad poblacional
        },
        "ciudades": [
            "São Paulo",
            "Río de Janeiro",
            "Brasilia"
        ],
        "superficie": 8515767  # Superficie en km²
    },
    {
        "nombre": "Paraguay",
        "capital": "Asunción",
        "moneda": "Guaraní",
        "poblacion": {
            "censo": 7,  # Población en millones
            "densidad": 18  # Densidad poblacional
        },
        "ciudades": [
            "Asunción",
            "Ciudad del Este",
            "Encarnación"
        ],
        "superficie": 406752  # Superficie en km²
    }
]

#Recorriendo todos los paises 
for pais in paises:
    print("Ciudades principales")
    for ciudad in pais["ciudades"]:
     print("-",ciudad)

     print(pais["nombre"])
     print(pais["capital"])
     print(pais["poblacion"])
     print("-Censo:",
          pais["poblacion"]["censo"], 
          "millones")
     print("-Densidad:",
          pais["poblacion"]["densidad"], 
          "por metros cuadrados")
     print("Superficie",
           pais["superficie"],"por metros cuadrados")
    
     print(".............")
    
