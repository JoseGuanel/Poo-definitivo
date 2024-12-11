class Cafeteria:
    # Variable de clase: tasa de descuento inicial (10%)
    _tasa_descuento = 0.10

    def __init__(self, nombre):
        self.__nombre = nombre  # Nombre de la cafetería (privado)
        self.__menu = {}        # Menú de productos y precios (privado)
        self.__pedidos = []     # Lista de pedidos de productos (privado)

    # Método de instancia para agregar un producto al menú
    def agregar_producto_menu(self, producto, precio):
        assert precio > 0, "Error: El precio debe ser mayor a cero"  # Invariante: precio positivo
        if producto not in self.__menu:
            self.__menu[producto] = precio
        else:
            print(f"El producto '{producto}' ya existe en el menú.")

    # Método de instancia para agregar un producto al pedido
    def agregar_producto_pedido(self, producto):
        assert producto in self.__menu, f"Error: El producto '{producto}' no está en el menú"  # Invariante: producto en menú
        self.__pedidos.append(producto)  # Agrega el producto al pedido

    # Método de instancia para calcular el total del pedido actual
    def calcular_total(self, frecuente=False):
        total = sum(self.__menu[producto] for producto in self.__pedidos)  # Suma precios de productos en el pedido
        if frecuente:
            total = self.calcular_precio_descuento(total, self._tasa_descuento)  # Aplica descuento si es cliente frecuente
        return total

    # Método estático para calcular un precio con descuento
    @staticmethod
    def calcular_precio_descuento(monto, descuento):
        assert 0 <= descuento <= 1, "Error: El descuento debe estar entre 0 y 1"  # Validación del descuento
        return monto * (1 - descuento)

    # Métodos de acceso para visualizar el menú y los pedidos
    @property
    def menu(self):
        return self.__menu

    @property
    def pedidos(self):
        return self.__pedidos

    # Propiedad para acceder a la tasa de descuento
    @property
    def tasa_descuento(self):
        return self.__class__._tasa_descuento  # Retorna la tasa de descuento

    # Método para cambiar la tasa de descuento de la clase
    @tasa_descuento.setter
    def tasa_descuento(self, nuevo_descuento):
        assert 0 <= nuevo_descuento <= 1, "Error: El descuento debe estar entre 0 y 1"
        self.__class__._tasa_descuento = nuevo_descuento  # Modifica la tasa de descuento

# Ejemplo de uso
cafeteria = Cafeteria("Café del Sol")
cafeteria.agregar_producto_menu("Café", 1500)
cafeteria.agregar_producto_menu("Té", 1200)
cafeteria.agregar_producto_menu("Sandwich", 2500)

# Agregar productos al pedido
cafeteria.agregar_producto_pedido("Café")
cafeteria.agregar_producto_pedido("Té")

# Cambiar la tasa de descuento
cafeteria.tasa_descuento = 0.15

# Calcular el total con y sin descuento
print(f"Total sin descuento: {cafeteria.calcular_total()}")
print(f"Total con descuento para cliente frecuente: {cafeteria.calcular_total(frecuente=True)}")

print(cafeteria.menu)

