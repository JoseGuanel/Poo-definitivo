
from datetime import datetime

class ReservaHostal():
    def __init__(self, cliente, ingreso, salida, habitacion):
        self.cliente = cliente
        self.ingreso = ingreso
        self.salida = salida
        self.habitacion = habitacion


    def estadia(self):
        return print(f"la duracion de la estadia es de {((self.salida - self.ingreso).days)} Dias")
    
    def __str__(self):
        return f"Nombre del cliente = {self.cliente} \nIngreso = {self.ingreso.strftime('%d/%m/%Y')} \nSalida = {self.salida.strftime('%d/%m/%Y')} \nN de habitacion = {self.habitacion}"

    def cambio(self,nueva_salid):
        self.salida = nueva_salid
    
    def __del__(self):
        print("reserva Cancelada")


reserva = ReservaHostal("Sancho panza", datetime(2024,10,10) ,datetime(2024,10,20), "5A")

#calcula la estadia
reserva.estadia()

#Muestra todos los datos de la reserva
print(reserva)

#Cambia la fecha de salida
reserva.cambio(datetime(2024,10,12))

