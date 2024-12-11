#ejercicio propuesto n4 
# Clase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__disponible = True

    # Método para marcar el vehículo como vendido
    def marcar_vendido(self):
        if self.__disponible:
            self.__disponible = False
            print(f"El vehículo {self.__marca} {self.__modelo} ha sido vendido.")
        else:
            print(f"El vehículo {self.__marca} {self.__modelo} ya está vendido.")
    
    # Método para mostrar los detalles del vehículo
    def __str__(self):
        estado = "Disponible" if self.__disponible else "No disponible"
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__año}, Estado: {estado}"

    # Método para saber si el vehículo está disponible
    def esta_disponible(self):
        return self.__disponible


# Clase Concesionaria
class Concesionaria:
    def __init__(self):
        self.vehiculos = []

    # Método para agregar un vehículo
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"Vehículo {vehiculo} agregado a la concesionaria.")

    # Método para mostrar todos los vehículos disponibles
    def mostrar_vehiculos(self):
        print("Vehículos disponibles:")
        for vehiculo in self.vehiculos:
            if vehiculo.esta_disponible():
                print(vehiculo)

    # Método para vender un vehículo
    def vender_vehiculo(self, marca, modelo):
        for vehiculo in self.vehiculos:
            if vehiculo.esta_disponible() and vehiculo.__str__().find(marca) != -1 and vehiculo.__str__().find(modelo) != -1:
                vehiculo.marcar_vendido()
                return
        print(f"El vehículo {marca} {modelo} no está disponible o ya fue vendido.")


# Interacción

# Crear la instancia de la concesionaria
concesionaria = Concesionaria()

# Agregar vehículos a la concesionaria
vehiculo1 = Vehiculo("Toyota", "Corolla", 2020)
vehiculo2 = Vehiculo("Ford", "Fiesta", 2018)
vehiculo3 = Vehiculo("Honda", "Civic", 2021)

concesionaria.agregar_vehiculo(vehiculo1)
concesionaria.agregar_vehiculo(vehiculo2)
concesionaria.agregar_vehiculo(vehiculo3)

# Mostrar los vehículos disponibles
concesionaria.mostrar_vehiculos()

# Realizar la venta de un vehículo
concesionaria.vender_vehiculo("Toyota", "Corolla")

# Volver a mostrar los vehículos disponibles
concesionaria.mostrar_vehiculos()
