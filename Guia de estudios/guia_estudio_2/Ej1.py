#Una empresa de eventos desea implementar un sistema que gestione la venta de
#tickets, calcule los ingresos y administre un descuento especial para tickets
#compra
"""Variables de Clase
Crear un descuento por compras en grupo, inicializado en 20%
Encapsulacion y Atributos Privados
 Crear un diccionario que guarda el tipo de ticket y su precio.
 Crear una lista de ventas registradas.
Interfaz y Metodos
Crear un metodo que agregue un tipo de ticket al sistema.
 Crear un metodo que registra la venta de tickets. Se debe asegurar de que el tipo de ticket
exista utilizando asertos
Metodos Estaticos y Asertos
 Crear un metodo estatico que calcule el total de la venta considerando el descuento de
grupo.
Especificacion e Invariantes
 Asegurar que todos los precios sean positivos y que el tipo de ticket exista antes de la venta.
Aplicar los conceptos de variables de clase, encapsulacion, asertos y metodos estaticos en un
sistema de venta de tickets para eventos."""

class Empresa():
    descuento = 0.20  # 20% de descuento para compras en grupo

    def __init__(self):
        # Atributos privados para tipos de tickets y sus precios
        self.__tipo_ticket = []      # Lista para almacenar los tipos de tickets
        self.__precio_ticket = []    # Lista para almacenar los precios correspondientes
        self.__ventas = []           # Lista para registrar las ventas

    def agregar_tipo_ticket(self, tipo, precio):
        """Agrega un nuevo tipo de ticket al sistema con su precio."""
        # Verificar que el precio sea positivo
        assert precio > 0, "El precio debe ser positivo."

        # Verificar si el tipo de ticket ya existe (sin usar `not`)
        tipo_existe = False
        for i in range(len(self.__tipo_ticket)):
            if self.__tipo_ticket[i] == tipo:
                tipo_existe = True
                break

        # Solo agregar el ticket si no existe ya
        if tipo_existe == False:
            self.__tipo_ticket.append(tipo)
            self.__precio_ticket.append(precio)
            print(f"Ticket '{tipo}' agregado con precio ${precio}.")
        else:
            print(f"El tipo de ticket '{tipo}' ya existe.")

    def registro_venta_ticket(self, tipo, cantidad):
        """Registra la venta de un tipo de ticket, asegurando que exista."""
        # Asegurar que la cantidad sea positiva
        assert cantidad > 0, "La cantidad de tickets debe ser positiva."

        # Buscar el índice del tipo de ticket
        tipo_index = -1
        for i in range(len(self.__tipo_ticket)):
            if self.__tipo_ticket[i] == tipo:
                tipo_index = i
                break

        # Verificar que el tipo de ticket exista
        assert tipo_index != -1, f"El tipo de ticket '{tipo}' no existe."

        # Registrar la venta
        self.__ventas.append((tipo, cantidad))
        print(f"Venta registrada: {cantidad} tickets de '{tipo}'.")

    @staticmethod
    def calcular_total_venta(precio_unitario, cantidad, descuento):
        """Calcula el total de la venta aplicando el descuento si corresponde."""
        subtotal = precio_unitario * cantidad
        if cantidad > 10:  # Aplicar descuento para grupos
            subtotal = subtotal * (1 - descuento)
        return subtotal

    def calcular_ingresos(self):
        """Calcula el ingreso total de todas las ventas registradas."""
        total = 0
        for tipo, cantidad in self.__ventas:
            # Encontrar el precio del tipo de ticket
            tipo_index = -1
            for i in range(len(self.__tipo_ticket)):
                if self.__tipo_ticket[i] == tipo:
                    tipo_index = i
                    break
            
            # Calcular total de la venta si el tipo de ticket existe
            if tipo_index != -1:
                precio_unitario = self.__precio_ticket[tipo_index]
                total = total + self.calcular_total_venta(precio_unitario, cantidad, Empresa.descuento)
        return total

# Ejemplo de uso
empresa = Empresa()
empresa.agregar_tipo_ticket("VIP", 100)
empresa.agregar_tipo_ticket("General", 50)

empresa.registro_venta_ticket("VIP", 5)
empresa.registro_venta_ticket("General", 12)

# Calcular ingresos totales
ingresos = empresa.calcular_ingresos()
print(f"Ingresos totales: ${ingresos}")