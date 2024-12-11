#Ejercicio unidad 3 
"""Contexto
Una empresa está desarrollando un sistema de gestión de pagos para su plataforma
de comercio electrónico. La plataforma admite diferentes métodos de pago, como
tarjetas de crédito, transferencias bancarias y pagos en efectivo. Cada método de
pago tiene un comportamiento diferente. Por ejemplo:
1.Las tarjetas de crédito necesitan ser validadas antes de procesar el pago.
Las transferencias bancarias requieren un código de confirmación antes de
completar la transacción.
2.
Los pagos en efectivo no necesitan validación ni confirmación, solo deben registrar
el monto recibido.
3.
Actualmente, la clase base MetodoDePago() incluye un método procesar_pago() que
asume que todos los métodos de pago deben validarse antes de procesarse. Sin
embargo, este diseño está causando problemas, ya que los pagos en efectivo no
necesitan validación, y algunos métodos de pago están lanzando excepciones
inesperadas.
EJERCICIO PRÁCTICO
Problema a Resolver
El sistema actual viola el Principio de Sustitución de Liskov (LSP) porque no todos los
métodos de pago respetan el comportamiento esperado de la clase base.
Tu tarea es rediseñar la jerarquía de clases para que los métodos de pago cumplan
con el LSP, asegurando que las subclases puedan ser utilizadas de forma
intercambiable sin romper el programa."""

# Clase base sin ABC
class MetodoDePago:
    def procesar_pago(self, monto):
        # Este método se deja vacío para que las subclases lo implementen
        raise NotImplementedError("Subclases deben implementar este método.")

# Clase para pagos con tarjeta de crédito
class PagoConTarjeta(MetodoDePago):
    def procesar_pago(self, monto):
        self.validar_tarjeta()
        self.efectuar_pago(monto)
        print(f"Pago con tarjeta procesado: {monto} unidades")

    def validar_tarjeta(self):
        print("Validando tarjeta de crédito...")

    def efectuar_pago(self, monto):
        print(f"Pago de {monto} unidades realizado con tarjeta de crédito.")

# Clase para pagos con transferencia bancaria
class PagoConTransferencia(MetodoDePago):
    def procesar_pago(self, monto):
        self.validar_transferencia()
        self.efectuar_pago(monto)
        print(f"Pago con transferencia bancaria procesado: {monto} unidades")

    def validar_transferencia(self):
        print("Solicitando código de confirmación de transferencia...")

    def efectuar_pago(self, monto):
        print(f"Pago de {monto} unidades realizado por transferencia bancaria.")

# Clase para pagos en efectivo
class PagoEnEfectivo(MetodoDePago):
    def procesar_pago(self, monto):
        self.registrar_pago(monto)
        print(f"Pago en efectivo procesado: {monto} unidades")

    def registrar_pago(self, monto):
        print(f"Registrando pago en efectivo de {monto} unidades.")

# Función para procesar el pago sin importar el método de pago
def procesar_pago(metodo_pago, monto):
    metodo_pago.procesar_pago(monto)

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear instancias de los métodos de pago
    tarjeta = PagoConTarjeta()
    transferencia = PagoConTransferencia()
    efectivo = PagoEnEfectivo()

    # Procesar pagos con distintos métodos
    procesar_pago(tarjeta, 100)
    procesar_pago(transferencia, 200)
    procesar_pago(efectivo, 50)


