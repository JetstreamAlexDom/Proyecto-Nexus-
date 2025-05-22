 # 1.- ---------------- Encabezado ----------------------------------------------
'''
Programa: Grafo de habilidades
Autor: Jorge Anzaldo.
Modificado por : Dominguez Flores Alejandro, Uriel Alberto Rodriguez y Velazquez Torres Diego
Grupo: 2CV14
Boleta: 2025300249
Fecha: 19/05/2025
Descripción: Este programa permite identificar y aplicar los grafos y los algoritmos de busqueda
Fecha de modificación :
Hora :
'''
# 2.- ---------------- Importación de Módulos y Bibliotecas --------------------
import networkx as nx
import matplotlib.pyplot as plt
# 3.- ---------------- Definición de Funciones o clases ------------------------
# Menu interactivo principal
print("\n--- BIENVENIDO A TU AVENTURA RPG ---\n")

#Pedir al usuario su nombre
nombre = input ("Ingrese su nombre de usuario -> ")

#Seleccionar genero
genero = ""
while genero.lower() not in ["masculino", "femenino"]: #lo que hace el ' .lower() ' es que convierte cualquier cadena a minusculas
    genero = input("Selecciona tu genero (masculino o femenino) -> ")

#Seleccionar especie con bonus
  #cada especie en el juego con el que me baso tiene un bonus distinto dependiendo de la especie

especies = { #En esta parte se usa un diccionario donde como clave tenemos el nombre de la especie y luego se ' anida ' otro diccionario como valor el cual tambien tiene ' C : V '  :)
    "humano" : {"bonus" : 1, "descripcion" : "La raza humana es la mas numerosa y poderosa de Thedas. Tambien es la que esta mas dividida politicamente y la que parece mas sedienta de conflictos. Los personajes humanos reciben un bonus de un punto de tecnica al inicio de la partida"},
    "elfos" : {"bonus" : 2, "descripcion" : "Los elfos han sido un pueblo historicamente orpimido, aunque en su mayoria sobreviven en los barrios mas pobres de las ciudades humanas. Los elfos reciben un 25% de bonus de defensa a distancia"},
    "enano" : {"bonus" : 3, "descripcion" : "Los enanos son bajos, fornidos y en su mayoria se pasan la vida entera bajo el suelo, no tienen ninguna conexion con el velo, asi que no pueden ser magos. Aunque reciben un bonus del 25% de defensa magica"},
    "qunari" : {"bonus" : 4, "descripcion" : "Los Qunari son una raza de gigantes cornudos que siguen un texto religioso muy estricto, el Qun. Los personajes Qunari reciben un bonus de 10% a la resistencia al daño fisico"}
}

print ("\nEspecies displonibles: ")
for especie, datos in especies.items(): # El ' .items() ' se usa para iterar sobre un ' {} ' y acceder a la vez a sus elementos ' C : V ' en este caso sirvio para mostrar las opciones disponibles
    print (f" -> {especie.capitalize()}: {datos['descripcion']} (Bonus: +{datos['bonus']} puntos de habilidad) ") # En esta parte lo que hace el ' capitalize() ' es que convierte la primer letra de un caracter a MAYUSCULA y las demas en minuscula
# especie: la clave (humano, mago, etc )
# datos : El valor para cada especie (ejemplo; "bonus" : 1, "descripcion" : "La raza humana es...."")

especie = " "
while especie.lower() not in especies:
    especie = input ("\nSelecciona tu especie -> ").lower()

#Seleccion de clase
clases = { #En esta parte se usa un diccionario (donde se usa el ' CLAVE (nombre) : VALOR (descripcion)' ) para acceder mas facil a la informacion de cada raza (y despues clase), en lugar de usar una lista donde se tendria que reocrrer uno por uno :)
    "picaro (dos armas)" : {"descripcion" : "Los picaros son luchadores que en vez de usar armadura pesada, confian en la velocidad y la agilidad. Pueden atacar de cerca con dagas para infligir un daño increible"},
    "picaro (arquero)" : {"descripcion": "Los picaros son luchadores que en vez de usar armadura pesada, confian en la velocidad y la agilidad. Pueden disparar flechas desde la distancia."},
    "guerrero (arma y escudo)" : {"descripcion" : "Los guerreros son combatientes de primera linea y pueden resistir fuertes golpes gracias a su armadura pesada. Pueden usar un arma junto con un escudo para incrementar su defensa"},
    "mago" : {"descripcion" : "Los magos canalizan el poder magico en hechizos que pueden tener diferentes efectos, desde debilitar a los adversarios hasta proteger a los aliados o liberar una energia devastadora"}
}

print ("\nClases disponibles: ")
for clase, datos in clases.items(): # El ' .items() ' se usa para iterar sobre un ' {} ' y acceder a la vez a sus elementos ' C : V ' en este caso sirvio para mostrar las opciones disponibles
    print (f"-> {clase.capitalize()}: {datos['descripcion']}")
# Clase: la clave (guerrero, mago, etc )
# Valor: la descripcion de cada clase

clase = " "
while clase.lower() not in clases:
    clase = input ("\nSelecciona tu clase -> ").lower()

#bonus segun la especie
bonus = especies [especie] ["bonus"]
print (f"\n Bienvenido, {nombre}. Eres un {especie} {genero} de clase {clase}. Recibes +{bonus} puntos de habilidad como bonificacion!\n")

#habilidades para el grafo segun la clase
habilidades_clase = { #EN esta parte como en una anterior se usaron diccionarios anidados para tener cada clase de una manera ordenada y tener todo organizado segun la clase con sus habilidades
    "guerrero (arma y escudo)" : {
        "Golpe venganza": 0,              #La CLAVE es el nombre de la habilidad (eje: "Golpe venganza");
        "Muro de escudos": 1,             # El VALOR es lo que define las propiedades tipo costo
        "Golpe de escudo":  1,            # Esto permite una organizacion clara (y tener las habilidades agrupadas segun la clase en un lugar) yyy tener un acceso rapido para el coste de cada una de ellas
        "Embestida y tajo": 2,
        "Guardaespaldas": 3,
        "Te costara": 3,
        "Fortaleza caminante": 5,
    },
    "picaro (dos armas)" : {
        "Ataque de flanco": 0,
        "Colmillos gemelos": 2,
        "Golpe letal": 3,
        "Sigilo": 2,
        "Cuchillas de hilatura": 3,
        "Cuchillas ocultas": 3,
        "Capa de sombras": 6

    },
    "picaro (arquero)": {
        "Primera sangre": 0,
        "Muerte desde las alturas": 1,
        "Tiro largo": 1,
        "Envenenamiento": 2,
        "Foco de lluvia de flechas": 5,
    },
    "mago": {
        "Claridad de combate": 0,
        "Inmolar": 1,
        "Paso de fundido": 1,
        "Tromba de energia": 2,
        "Espada espiritual" : 2,
        "Capa de desvanecimiento" : 3,
        "Enfoque de resurgimiento" : 5,
    }
}

# conexiones para el grafo segun la clase

conexiones_clase = { # En esta parte se usaron ' {} ' anidados para organizar las conexiones de la clase yy LISTAS ' [] ' para definir las relaciones entre las habilidades dentro de cada clase
    "guerrero (arma y escudo)" : [
        ("Golpe venganza", "Muro de escudos", 1),         # a su vez se usaron TUPLAS ' () '  (que son inmutables y sirven como el VALOR del diccionario) que representa;
        ("Golpe venganza", "Golpe de escudo", 1),         # ("habilidad de origen", "habilidad de destino", costo),  ejemplo;
        ("Muro de escudos", "Embestida y tajo", 2),       # ("Embestida y tajo",    "Fortaleza caminante",    5),
        ("Golpe de escudo", "Guardaespaldas",3),
        ("Guardaespaldas", "Te costara", 3),              # las tuplas en las listas hacen evidente la conexion entre las habilidades
        ("Embestida y tajo", "Fortaleza caminante", 5),
        ("Te costara", "Fortaleza caminante", 5),
    ],

    "picaro (dos armas)" : [
        ("Ataque de flanco", "Colmillos gemelos", 2),
        ("Colmillos gemelos", "Golpe letal", 3),
        ("Golpe letal", "Capa de sombras", 6),
        ("Ataque de flanco", "Cuchillas de hilatura", 3),
        ("Cuchillas de hilatura", "Cuchillas ocultas",3),
        ("Cuchillas ocultas", "Capa de sombras", 6),
        ("Cuchillas ocultas", "Sigilo", 2)


    ],

    "picaro (arquero)" : [
        ("Primera sangre", "Muerte desde las alturas", 1),
        ("Primera sangre", "Tiro largo", 1),
        ("Muerte desde las alturas", "Envenenamiento", 2),
        ("Tiro largo", "Tiro explosivo", 2),
        ("Tiro explosivo", "Foco de lluvia de flechas", 5),
    ],

    "mago" : [
        ("Claridad de combate", "Inmolar", 1),
        ("Claridad de combate", "Paso de fundido", 1),
        ("Inmolar", "Tromba de energia", 2),
        ("Paso de fundido", "Capa de desvanecimiento", 3),
        ("Tromba de energia", "Enfoque de resurgimiento", 5),
        ("Capa de desvanecimiento", "Enfoque de resurgimiento", 5),
        ("Capa de desvanecimiento", "Espada espiritual", 2),
    ],
}

#crear el grafooo

# --- CREAR GRAFO SEGÚN CLASE ---
G = nx.Graph() #creamos un grafo vacio
habilidades = habilidades_clase[clase]  #añadimos NODOS (habilidades) con sus atributos (costo)
for habilidad, costo in habilidades.items():
    G.add_node(habilidad, costo=costo) # cada NODO  es una habilidad con su costo como atributo

for a, b, peso in conexiones_clase[clase]:
    G.add_edge(a, b, peso=peso) # añadimos ARISTAS (conexiones) con pesos y representan las conexiones entre las habilidades
                                # el peso es el costo para desbloquear esa conexion y resulta util para los algporitmos de rutas, busqueda (giño giño)

# Sistema interactivo de elección
puntos = 10 + bonus
inicio = list(habilidades.keys())[0] # el ' .keys() ' se usa para validar las claves de un diccionatio
habilidades_desbloqueadas = [inicio]

print(f"\n=== ÁRBOL DE HABILIDADES DE {nombre.upper()} ({clase.upper()}) ===") #el ' .upper ' convierte una cadena a MAYUSCULAS
print(f"Inicias con {puntos} puntos de habilidad disponibles.\n")

while puntos > 0:
    print("Habilidades desbloqueadas:", habilidades_desbloqueadas)

    opciones = []
    for habilidad in habilidades_desbloqueadas:
        for vecino in G.neighbors(habilidad): # el ' .neighbords ' devuelve una lista de los nodos conectados directamente a un nodo 'vecino' y tiene como objetivo identificar que habilidades se pueden desbloquear desde las ya desbloqueadas
            if vecino not in habilidades_desbloqueadas:
                costo = G[habilidad][vecino]['peso']
                if (vecino, costo) not in opciones:
                    opciones.append((vecino, costo)) # el ' .append ' en esta parte añade la tupla (habilidad, costo) a la lista

    if not opciones:
        print("No hay más habilidades disponibles para desbloquear.")
        break

    print("\nOpciones disponibles:")
    for i, (habilidad, costo) in enumerate(opciones): # el ' enumerate() ' devuelve un iterador que genera pares (indice, elemento) para una lista,
        print(f"{i + 1}. {habilidad} (Costo: {costo})") # como objetivo para mostrar un menu numerado de opciones (ejemplo: 1. GOlpe letal (costo: 2))

    eleccion = input("Selecciona una habilidad por número (o 'salir'): ")
    if eleccion.lower() == 'salir':
        break

    if not eleccion.isdigit() or not (1 <= int(eleccion) <= len(opciones)): # el ' isdigit() ' verifica si una cadena solo tiene digitos,
        print("Opción no válida. Intenta de nuevo.\n")                      # se uso para validar que lo que ingrese el usuario sea un numero para seleccionar la hanilidad
        continue

    seleccionada, costo = opciones[int(eleccion) - 1]
    if costo > puntos:
        print("No tienes suficientes puntos para esa habilidad.\n")
        continue

    puntos -= costo
    habilidades_desbloqueadas.append(seleccionada)
    print(f"Habilidad '{seleccionada}' desbloqueada. Te quedan {puntos} puntos.\n")

print("\nÁrbol final de habilidades desbloqueadas:", habilidades_desbloqueadas)

# Dibujar el grafo para su visualizacion

pos = nx.spring_layout(G, seed=42)  # posicion de los NODOS
        # el ' spring_layout() ' organiza los NODOS en un formato organico (osea que evita superposiciones)

plt.figure(figsize=(12, 8))
colores = ['lightgreen' if nodo in habilidades_desbloqueadas else 'lightgray' for nodo in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_color=colores, node_size=1500)
nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')
nx.draw_networkx_edges(G, pos, width=2)
labels = nx.get_edge_attributes(G, 'peso')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)


plt.title(f"Árbol de Habilidades - Clase {clase.capitalize()}")
plt.axis('off')
plt.tight_layout()
plt.show()

# 6.- ---------------- Documentación y Comentarios------------------------------
# lIGA DE LA PRESENTACION GAMMA APP
# https://gamma.app/docs/Dominando-la-Curva-Un-Sistema-de-Habilidades-Revolucionario-bnwpqfw1yho2p3f