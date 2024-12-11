# EJERCIICIO DE DUCK  TYPING
import math

# Clase Círculo
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

# Clase Rectángulo
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

# Clase Triángulo
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return 0.5 * self.base * self.altura

# Clase Cuadrado (es un caso especial de rectángulo)
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

# Clase Trapecio
class Trapecio:
    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def calcular_area(self):
        return 0.5 * (self.base_mayor + self.base_menor) * self.altura

# Clase Pentágono Regular
class PentagonoRegular:
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema

    def calcular_area(self):
        return 5 * self.lado * self.apotema / 2

# Función mostrar_area
def mostrar_area(figura):
    print(f"El área de la figura es: {figura.calcular_area()}")

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear instancias de las figuras
    circulo = Circulo(5)
    rectangulo = Rectangulo(4, 6)
    triangulo = Triangulo(5, 8)
    cuadrado = Cuadrado(4)
    trapecio = Trapecio(8, 5, 6)
    pentagono = PentagonoRegular(6, 7)

    # Mostrar el área de cada figura
    mostrar_area(circulo)
    mostrar_area(rectangulo)
    mostrar_area(triangulo)
    mostrar_area(cuadrado)
    mostrar_area(trapecio)
    mostrar_area(pentagono)
