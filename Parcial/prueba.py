import random
class Gato():
    def __init__(self,nombre,edad,color,energia,hambre,estado):
        self.nombre=nombre
        self.__edad=edad
        self.__color=color
        self.energia=energia
        self.hambre=hambre
        self.estado=estado
    def jugar(self,estado):
        if estado == "Hambriento/cansado":
            print(f"{self.nombre} esta cansado y hambriento, no quiere jugar.")
        else:  
            print(f"{self.nombre} esta jugando contigo. -20 energia +10 hambre")
            self.energia-= 20
            self.hambre-= 10
            inv.stock_juguete-= 1
            print(f"Pelota pinchada quedan {inv.stock_juguete} pelotas en stock")
    def acariciar(self):
        if self.estado == "Hambriento/cansado":
            print(f"El gato esta cansado y hambriento, no quiere jugar.")
        else:
            print(f"le estas haciendo caricias a {self.nombre}. -10 energia")
            self.energia-= -10
    def alimentar(self):
        print(f"Le estas dando {inv.comida} a {self.nombre}. -10 de hambre")
        inv.stock_churu-= 1
        print(f"Quedan {inv.stock_churu} churus en el inventario")

    def inf_estado(self):
        if self.hambre>=50:
            self.estado="Hambriento"
        if self.energia<=50:
            self.estado="Cansado"
        else:
            self.estado= "Contento o saciado"
        return self.estado
    def __str__(self):
        return f"Nombre:{self.nombre} Edad:{self.__edad} año/s Color:{self.__color} Energia:{self.energia}/100 Hambre:{self.hambre}/100 Estado: {self.estado}."
class Area():
    def __init__(self, lugar,capacidad, capacidad_max):
        self.lugar=lugar
        self.capacidad=capacidad
        self.capacidad_max=capacidad_max
    def agregar_gato(self, nombre):
        if len(self.capacidad) != self.capacidad_max:
            self.capacidad.append(nombre)
    def gatos_en_area(self):
        print(f"En {self.lugar} estan los siguientes gatos: {self.capacidad}")

class Inventario():
    def __init__(self, juguete, comida, stock_juguete, stock_churu):
        self.juguete=juguete
        self.comida=comida
        self.stock_juguete=stock_juguete
        self.stock_churu=stock_churu
    def agrega_stock_churu(self,cantidad):
        self.stock_churu += cantidad
    def agrega_stock_juguete(self,cantidad):
        self.stock_juguete+= cantidad


#Inventario local
inv=Inventario("pelota de ratón", "churu", 10,10)
#CREACION DE GATOS
gato1=Gato("Juanito",2,"Naranja", random.randint(1,100), random.randint(1,100),"")
gato2=Gato("Pepe", 3,"Negro", random.randint(1,100), random.randint(1,100),"")
gato3=Gato("Victor",7,"Blanco", random.randint(1,100), random.randint(1,100),"")

###AREA 1
area1=Area("Terraza", [], 5)
area1.agregar_gato(gato1.nombre)
area1.gatos_en_area()

##AREA 2
area2=Area("Interior", [], 10)
area2.agregar_gato(gato2.nombre)
area2.agregar_gato(gato3.nombre)
area2.gatos_en_area()

#Interacciones gatos

print(gato1.inf_estado())

gato1.jugar(gato1.inf_estado())
gato1.alimentar()


gato2.jugar(gato2.inf_estado())

gato3.jugar(gato3.inf_estado())
print(gato1)
print(gato2)
print(gato3)