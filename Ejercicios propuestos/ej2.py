class Coche:
    def __init__(self, marca, gasolina):
        self.marca = marca
        self.gasolina = gasolina
        self.kilometros_recorridos = 0

    def conducir(self, kilometros):
        
        gasolina_necesaria = kilometros / 10
        
        # revisarsuficiente gasolina
        if gasolina_necesaria <= self.gasolina:

            print(f"Has conducido {kilometros} kilómetros. Te quedan {self.gasolina - gasolina_necesaria} litros de gasolina.")
        else:
            kilometros_recorridos = self.gasolina * 10
            self.gasolina= 0
            print(f"Te has quedado sin gasolina después de recorrer {kilometros_recorridos} kilómetros. Necesitas {gasolina_necesaria - (kilometros_recorridos/10) }" )
            x=int(input("Cuantos litros desea cargar?: "))
            self.cargar_gasolina(x, kilometros)

    def cargar_gasolina(self, litros, km):
        self.gasolina = litros
        print(f"Has agregado {litros} litros de gasolina. Ahora tienes {self.gasolina} litros de gasolina.")
        self.conducir(km - self.kilometros_recorridos)

#uso de la clase coche
mi_coche = Coche("chevrolet", 5)  # Creamos un coche (objeto) con 10 litros de gasolina

# Conducimos 50 kilómetros
mensaje = mi_coche.conducir(60)
