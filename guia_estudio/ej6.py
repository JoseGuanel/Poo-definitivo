
"""
. Mediante el uso de clases, modelar el movimiento rectilíneo uniforme (MRU) de un objeto
utilizando la programación orientada a objetos. Se deben implementar dos clases: Cuerpo,
que representa un objeto en movimiento con velocidad constante, y SimuladorMovimiento,
que se encargará de simular y graficar el movimiento del objeto en función del tiempo.
La clase Cuerpo debe modelar un objeto en movimiento con una velocidad constante.
Mientras que la clase SimuladorMovimiento simula el movimiento y grafica la posición del
objeto en función del tiempo utilizando la fórmula del MRU.
Fórmula del MRU:
𝑥 = 𝑥0 + 𝑣𝑡


"""

#Ahi abri los otros ejercicios en live share pa que los veas si quieres | dale gracias

import matplotlib.pyplot as plt 
import numpy as np

class Cuerpo(): # el cuerpo tendra una velocidad constante pero que estará en movimiento.
    def __init__(self,velocidad_c,posicion_inicial):
        self.velocidad = velocidad_c
        self.posicion_inicial = posicion_inicial


    def posicion(self,tiempo): # formula de posicion= Xf = xo + velocidad * tiempo
        return self.posicion_inicial +self.velocidad * tiempo 



# aca es con grafico porrsia con el plot
class SimuladorMovimiento():
    def __init__(self,cuerpo,tiempo, intervalos=100):
        self.cuerpo = cuerpo
        self.tiempo = tiempo
        self.intervalos = intervalos 

    def simular(self):
        tiempo_f = np.linspace(0, self.tiempo,self.intervalos) # así tenemos un tiempo máximo
        posiciones = [self.cuerpo.posicion(t) for t in tiempo_f] 

        plt.plot(tiempo_f, posiciones, label=" Velocidad = {self.cuerpo.velocidad} m/s")
        plt.xlabel("tiempo (segundos)")
        plt.ylabel("posicion (metros)")
        plt.title("Simulación MRU")
        plt.grid(True)
        plt.legend()
        plt.show()

pelota = Cuerpo(posicion_inicial=0, velocidad_c=5)

# Crear el simulador para simular hasta 20 segundos
simulador = SimuladorMovimiento(pelota, tiempo=20)

# Imprimir información del cuerpo
print(pelota)

# Ejecutar la simulación y graficar
simulador.simular()