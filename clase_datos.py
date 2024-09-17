class informacion:

    def mi_lista(self):
        print("Lista")
        lista_Nomperros=["boby", "dollar", "fany"]
        print(lista_Nomperros)
        for x in lista_Nomperros:
            print(x)
        print("-----------------------------------------------")

    def mi_tupla(self):
        print("Tuplas")
        tuplas_Nomgatos=("raul", "michi", "teru")
        print(tuplas_Nomgatos)
        for x in tuplas_Nomgatos:
            print(x)
        print("-----------------------------------------------")

    def mi_conjunto(self):
        print("Conjuntos")
        conjunto_razaperros={"chihuahua", "salchicha", "pug"}
        print(conjunto_razaperros)
        for x in conjunto_razaperros:
            print(x)
        print("-----------------------------------------------")

    def mi_diccionario(self):
        print("Diccionario")
        diccionario_colorperros={
            "color_1": "negro", 
            "color_2": "gris", 
            "color_3": "blanco"
        }
        print(diccionario_colorperros)
        for x,y in diccionario_colorperros.items():
            print(x,y)
        print("-----------------------------------------------")

# Creando el objeto
datos=informacion()
print("Listado de nombre de perro")
datos.mi_lista()
datos.mi_tupla()
datos.mi_conjunto()
datos.mi_diccionario()