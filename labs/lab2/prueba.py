"""1. Encapsulación de Datos del Cliente
A. ¿Qué datos del cliente crees que deben encapsularse en una clase Cliente?
Considera atributos como el tipo de cliente (estudiante, académico, otro) y el
precio de la compra. ¿Cuál de estos atributos debería ser privado y cuál
público? ¿Por qué?
r: El nombre para identificarse y rut para identificarse de mejor manera ya que el nombre y apellido se pueden repetir,
el tipo de cliente para aplicar el descuento si tiene, y el precio de la compra que hará,
los atributos privados deberian ser el nombre y el rut ya que es una informacion personal que solo sirve
para identificarse y corroborar el tipo de cliente.
"""
"""
2. Diccionario de Descuentos
A. ¿Cómo organizarías los descuentos disponibles para cada tipo de cliente en
el sistema? ¿Crees que un diccionario privado podría ser útil para almacenar
los descuentos para cada tipo de cliente? ¿o se necesita otro tipo de
estructura de datos?
B. ¿Por qué sería útil encapsular la estructura de datos anterior de descuentos
en lugar de exponerlo directamente?

r: Yo no usaria un diccionario solamente para aplicar un descuento ya que solo hay 3 opciones, estudiante, profesor y otro,
usara un if, elif y else, y menos un diccionario privado ya que es una información no relevante para mantener privado como podria ser
el rut o datos del cliente"""

"""Variables de Clase
1. Definición de Descuentos
A. ¿Cómo definirías los descuentos para cada tipo de cliente en el sistema?
Considera que el descuento para los estudiantes es del 20% y para los
académicos del 10%.
R: no los definiria como tal, basta con un "Mientras seas este tipo, te descuento tal porcentaje", al ser solo 3 tipos
no es necesario crear un diccionario para designar los descuentos por tipo de cliente

Programación Orientada a Objetos Laboratorio N°2
B. ¿Crees que estos descuentos deberían ser variables de clase o variables de
instancia? Justifica tu respuesta en términos de reutilización y claridad del
sistema.
R: variables de instancia ya que si fuera una variable de clase (cliente), seria siempre el mismo descuento sin importar que tipo
de cliente sea ya que está fuera del init donde va el tipo de cliente, es decir no se podria modificar, es mejor llamar al descuento
cuando ya tienes tu tipo de cliente y estas calculando el precio total.

1. Métodos para Modificar el Precio de Compra
A. ¿Cómo permitirías la modificación del precio de la compra de un cliente sin
que se afecte la lógica de descuentos? ¿Crees que sería útil usar un setter
para ajustar el precio antes de aplicar el descuento?

R: Seria util si la variable precio fuera privada, al no ser privada se puede modificar simplemente reescribiendo el valor de la variable.

B. ¿Qué tipo de acceso debería tener el descuento del cliente? ¿Cómo un getter
podría facilitar la obtención del precio final sin exponer el cálculo interno?

R: publico, ya que los descuentos que hace el casino deberia ser publico, por ejemplo que haya 20% de descuento para estudiantes
10% para los academicos, no hay mucho para ocultar en eso, no es necesario. por lo tanto exponer el calculo interno que seria la 
aplicacion de este descuento daria igual.


Métodos Estáticos
1. Cálculo del Precio Final
A. Imagina que deseas implementar un método que calcule el precio final
después de aplicar el descuento correspondiente. ¿Por qué sería conveniente
implementar este método como un método estático?

R: para usar menos recursos ya que no es necesario usar las variables y datos que tenemos en el codigo, solo usar el
metodo, entonces haciendolo un metodo estatico se usaria menos memoria para simular.
B. ¿Qué ventajas tiene usar un método estático en este caso, en comparación
con un método de instancia?
R: la principal ventaja es que no usas datos del __init__ ni de fuera de la clase, son variables que se instancian ahi por lo cual
el uso de memoria es mas baja. 
2. Implementación del Descuento
A. Si decides crear un método estático ¿qué parámetros debería recibir este
método y qué valor debería devolver? ¿Por qué?
R: Si quisiera hacer un metodo estatico para calcular el precio final aplicando el descuento, usaria los parametros (precio,descuento)
y retornaria precio * descuento (si el descuento es de 10% el descuento que ingresaria sería 0.9 para evitar mas codificacion.)


Asertos e Invariantes
1. Verificación del Precio
A. ¿Qué asertos consideras que serían útiles para asegurar que el precio de una
compra no sea negativo? ¿Cómo evitarías que se realice una compra con un
valor incorrecto?

R: un assert que solo permita que el precio sea mayor que 0, assert precio > 0 , "Error, tu precio es menor que 0"

2. Control de Descuentos y Validación del Tipo de Cliente
A. ¿Qué invariante podrías establecer para asegurarte de que el descuento sólo
se aplica si el tipo de cliente es válido (es decir, estudiante o académico)?

B. ¿Cómo usarías asertos para verificar que el tipo de cliente ingresado esté
dentro de los tipos válidos antes de aplicar el descuento?:
R: assert self.tipo =="estudiante" or self.tipo =="academico" or self.tipo =="otro", "Error, tipo de cliente no valido"
, este ultimo (self.tipo=="otro") se podria evitar ya que uso if, elif y else al aplicar descuento, quiere decir que 
uso un else para el "otro", entonces si ingresara un tipo que no sea academico o estudiante, si ingresaran por ejemplo "Pajaro"
no habria descuento. 


"""



class Cliente():
    def __init__(self, __nombre, __rut,tipo,precio):
        self.__nombre= __nombre
        self.__rut=__rut
        self.tipo=tipo
        self.precio= precio

    def precio_total(self):
        assert self.tipo =="estudiante" or self.tipo =="academico" or self.tipo =="otro", "Error, tipo de cliente no valido"
        if self.tipo=="estudiante":
            print(f"El precio es de {self.precio}, como eres {self.tipo} se te descuenta un 20%.")
            self.precio= self.precio*0.80
            print(f"Precio: {self.precio} ")
        elif self.tipo=="academico":
            print(f"El precio es de {self.precio}, como eres {self.tipo} se te descuenta un 10%.")
            self.precio= self.precio*0.90
            print(f"Precio: {self.precio}")
        else:
            print(f"El precio es de {self.precio}. tipo: Otro ")

    
    
juan= Cliente("juan", "21327659-k", "otro", 5000)
juan.precio_total()
pedro=Cliente("pedro", "21314611-1", "estudiante", 10000)
pedro.precio_total()
victor=Cliente("victor","19121424-2", "academico", 31000)
victor.precio_total()
vicente=Cliente("vicente", "22331623-5", "estudiante", 2000)
vicente.precio_total()
benjamin=Cliente("benjamin", "21871844-k", "estudiante", 5000)
benjamin.precio_total()



        

