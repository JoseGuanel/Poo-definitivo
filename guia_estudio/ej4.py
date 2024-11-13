""" 4. Implementar una clase Pedido que represente un pedido en un restaurante. Cada pedido
tiene un número de mesa, una lista de platos pedidos y el total del costo del pedido.
Clase Pedido:
● Atributos:
○ Número de mesa, lista de platos, y el total del pedido. (listo)

● Métodos:
○ Crear método para añadir platos al pedido (cada plato tiene un nombre y un <-- listo
precio) 
○ Crear método para calcular el total del pedido. <-- listo
○ Implementar un método mágico para contar el número de platos en el <-- listo
pedido.
○ Implementar un método mágico para combinar dos pedidos de la misma
mesa (sumar platos y total).

● Finalizador:
○ Al eliminar un pedido, mostrar un mensaje indicando que el pedido ha sido
completado. """

class Pedido():
    def __init__(self, num_mesa): # el constructor
        self.num_mesa = num_mesa
        self.lista_platos = [] # creé lista vacía
        self.total_pedidos = 0.0 # total inicializado en 0 pesos

    def añadir_platos(self,nombre_plato,precio):
        self.lista_platos.append((nombre_plato,precio)) # se añade el nombre del plato y el precio y se añade a la lista creada en el la clase
        self.calcular_total() # para retornar el total de todo

    def calcular_total(self):
        self.total_pedidos = sum(precio for i, precio in self.lista_platos) 
    
    def __len__(self): # contar la cantidad de platos en el pedido de una mesa
        return len(self.lista_platos)

    def __add__(self,combinar_pedido):
        if self.num_mesa == combinar_pedido.num_mesa:
            nuevo_pedido= Pedido(self.num_mesa)
            nuevo_pedido.lista_platos = self.lista_platos + combinar_pedido.lista_platos
            nuevo_pedido.calcular_total()
            return nuevo_pedido
        
    def __del__(self):
        print(f"El pedido de la mesa {self.num_mesa} ya ha sido completado. gracias!")

# Iterando o creando los objetos
pedido1= Pedido(5)
pedido1.añadir_platos("Fideos",5000)
pedido1.añadir_platos("Arroz", 4000)
print(f" \n Precio total del pedido N°1 : {pedido1.total_pedidos} ")
print(f" Número de platos del pedido N°1: {len(pedido1)} \n")

pedido2 = Pedido(5) # creando otro objeto para poder combinar
pedido2.añadir_platos("Milcao",2500)

# funcion de combinacion de pedidos
combinar_pedido =   pedido1 + pedido2
print(f"El total del pedido combinado es: {combinar_pedido.total_pedidos} ")
print(f"El numero de platos en el nuevo pedido combinado es {len(combinar_pedido)} \n")