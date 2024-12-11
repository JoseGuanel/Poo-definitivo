#eJERCICI PROPUESTO EL PENULTIMO

class Animal(): # super clase / clase general
    def __init__(self,nombre,edad,peso,color,sonido):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.color = color
        self.sonido = sonido

    def comer(self):
        print(f"{self.name} está comiendo")

    def hacer_sonido(self):
        print(self.sonido)
    
class Perro(Animal):
    def __init__(self, nombre, edad, raza, peso, color, sonido):
        super().__init__(nombre, edad, peso, color, sonido)
        self.raza = raza
    
    def ladrar(self):
        print(f"{self.nombre} está ladrando")


    def info(self):
        print("Informacion del Perro: \n")
        print(f"Nombre: {self.nombre} \n edad: {self.edad} \n raza: {self.raza} \n peso: {self.peso} \n color: {self.color} \n sonido: {self.sonido} \n ")

class Gato(Animal):
    def __init__(self, nombre, edad, color_ojos, peso, color, sonido):
        super().__init__(nombre, edad, peso, color, sonido)
        self.color_ojos = color_ojos

    def maullar(self):
        print(f"{self.nombre} está maullando")

    def info(self):
        print("Informacion del Gato: \n")
        print(f"Nombre: {self.nombre} \n edad: {self.edad} \n color de ojos: {self.color_ojos} \n peso: {self.peso} \n color: {self.color} \n sonido: {self.sonido} \n ")


class Pajaro(Animal):
    def __init__(self, nombre, edad, peso, color, sonido, color_alas):
        super().__init__(nombre, edad, peso, color, sonido)
        self.color_alas = color_alas

    def volar(self):
        print(f"{self.nombre} está volando")

    def info(self):
        print("Informacion del Pajaro: \n")
        print(f"Nombre: {self.nombre} \n edad: {self.edad} \n peso: {self.peso} \n color de alas: {self.color_alas} \n color: {self.color} \n sonido: {self.sonido} \n ")
    
    

class Pez(Animal):
    def __init__(self, nombre, edad, peso, color, sonido, color_cola):
        super().__init__(nombre, edad, peso, color, sonido)
        self.color_cola = color_cola
        
    def nadar(self):
        print(f"{self.nombre} está nadando")

    def info(self):
        print("Informacion del Pez: \n")
        print(f"Nombre: {self.nombre} \n edad: {self.edad} \n peso: {self.peso} \n color de la cola: {self.color_cola} \n color: {self.color} \n sonido: {self.sonido} \n ")

    


# Creando instancias
perro1 = Perro("benja",19, "bulldog",20,"Blanco","GUAU")
gato1 = Gato("Rocio",27,"Verdes",5,"Blanco","MIAU")
pajaro1 = Pajaro("Vicente",18,1,"Amarillo","pio pio","Verdes")
pez1 = Pez("Jose",21,0.5,"Negro","GLU GLU","Rojo")

# sus instancias propias
perro1.ladrar()
gato1.maullar()
pajaro1.volar()
pez1.nadar()

# infos de cada animal
perro1.info()
gato1.info()
pajaro1.info()
pez1.info()

# métodos heredados
perro1.comer()
gato1.comer()
pajaro1.comer()
pez1.comer()
perro1.hacer_sonido()
gato1.hacer_sonido()
pajaro1.hacer_sonido()
pez1.hacer_sonido()