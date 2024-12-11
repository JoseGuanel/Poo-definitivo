#ej3
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        # Atributos privados
        self.__titular = titular  # Encapsulamos el titular
        self.__saldo = saldo_inicial  # Encapsulamos el saldo

    # Método para consultar el saldo (getter)
    def consultar_saldo(self):
        return self.__saldo

    # Método para depositar dinero
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("El monto debe ser mayor que cero.")

    # Método para retirar dinero
    def retirar(self, monto):
        if monto > self.__saldo:
            print("Fondos insuficientes.")
        elif monto <= 0:
            print("El monto a retirar debe ser mayor que cero.")
        else:
            self.__saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")

    # Getter para el titular
    def get_titular(self):  #Getters: Son para obtener o consultar el valor de un atributo privado.
        return self.__titular 
    # Setter para cambiar el titular
    def set_titular(self, nuevo_titular):   #Setters: Son para modificar el valor de un atributo privado de manera segura y controlada.

        if nuevo_titular:
            self.__titular = nuevo_titular
            print(f"Titular cambiado exitosamente a: {nuevo_titular}")
        else:
            print("El nombre del titular no puede estar vacío.")

# Ejemplo de uso
cuenta = CuentaBancaria("goku Perez", 1000)
print("Saldo inicial:", cuenta.consultar_saldo())
cuenta.depositar(500)
cuenta.retirar(300)
print("Titular de la cuenta:", cuenta.get_titular())
cuenta.set_titular("gohan andrade")
