class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        # cadena de la fracción
        return f"{self.numerador}/{self.denominador}"
    
    def __add__(self, frac):
        # Suma de dos fracciones: a/b + c/d = (a*d + b*c) / (b*d)
        nuevo_numerador = self.numerador * frac.denominador + self.denominador * frac.numerador
        nuevo_denominador = self.denominador * frac.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __mul__(self, frac):
        # multiplicacion de dos fracciones: a/b * c/d = (a*c) / (b*d)
        nuevo_numerador = self.numerador * frac.numerador
        nuevo_denominador = self.denominador * frac.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __eq__(self, frac):
        # Comparación de igualdad: a/b == c/d si y solo si a*d == b*c
        return self.numerador * frac.denominador == self.denominador * frac.numerador


# Ejemplo de uso:
frac1 = Fraccion(1, 2)
frac2 = Fraccion(2, 4)

print(frac1)            
print(frac2)          
print(frac1 + frac2)    
print(frac1 * frac2)  
print(frac1 == frac2) 

