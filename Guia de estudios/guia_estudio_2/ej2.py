class Gimnasio:
    descuento_anual = 0.10  # Descuento de 10% para suscripciones anuales

    def __init__(self, nombre_cliente, tipo_suscripcion, costo_base=100):
        self.__nombre_cliente = nombre_cliente
        self.set_tipo_suscripcion(tipo_suscripcion)
        self.set_costo(costo_base)

    # Accesores y mutadores
    def get_costo(self):
        return self.__costo

    def set_costo(self, nuevo_costo):
        assert nuevo_costo >= 0, "El costo no puede ser negativo."
        self.__costo = nuevo_costo

    def get_tipo_suscripcion(self):
        return self.__tipo_suscripcion

    def set_tipo_suscripcion(self, tipo):
        assert tipo in ["mensual", "trimestral", "anual"], "Tipo de suscripción inválido."
        self.__tipo_suscripcion = tipo
    
    def info (self) :
        return f"el cliente{self.__nombre_cliente} cuya mensualidad es de {self.get_tipo_suscripcion()}\n"        

    # Método estático para calcular el costo final
    @staticmethod
    def calcular_costo(costo_base, tipo_suscripcion):
        assert costo_base >= 0, "El costo no puede ser negativo."
        assert tipo_suscripcion == "mensual" or tipo_suscripcion == "trimestral" or tipo_suscripcion == "anual", "Tipo de suscripción inválido."

        
        if tipo_suscripcion == "mensual":
            return costo_base
        elif tipo_suscripcion == "trimestral":
            return costo_base * 3
        elif tipo_suscripcion == "anual":
            # Aplica el descuento del 10% solo para la suscripción anual
            costo_anual = costo_base * 12
            costo_con_descuento = costo_anual * (1 - Gimnasio.descuento_anual)
            return costo_con_descuento

# Ejemplo de uso
cliente = Gimnasio(nombre_cliente="condorito", tipo_suscripcion="anual", costo_base=150)

print(cliente.info())

# Llamar al método estático para calcular el costo
costo_final = Gimnasio.calcular_costo(cliente.get_costo(), cliente.get_tipo_suscripcion())
print("Costo final de la suscripción:", costo_final)
