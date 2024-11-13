import pygame
import random

pygame.init()

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Laboratorio N°2 - Ejercicio 2")


# Colores
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

# FPS (Frames por segundo)
FPS = 60
reloj = pygame.time.Clock()

class Puntos:
    def __init__(self, x, y, velocidad):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.radio = 8  # Tamaño del punto

    def mover(self):
        self.y += self.velocidad
        if self.y > ALTO:  # Se reinicia ka posición cuando el punto rojo sale de la pantalla
            self.reiniciar()

    def reiniciar(self):
        self.x = random.randint(0, ANCHO - self.radio)
        self.y = random.randint(-100, -40)

    def dibujar(self):
        pygame.draw.circle(pantalla, ROJO, (self.x, self.y), self.radio)

# Clase Triángulo
class Triangulo:
    def __init__(self, x,y, speed): #x posicion de inicio, y altura del triangulo, speed la velocidad.
        self.x=x
        self.y=y
        self.speed=speed
    def mover(self, keys):
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
    def dibujar(self):
        pygame.draw.polygon(pantalla, (0,0,255), [(self.x + 200, 600-self.y),(self.x + 150,600),(self.x +250,600)])

    # def detecta_col(self):
        
# Función Principal
def main():
    # Creación de la lista de puntos rojos
    puntos_rojos = [Puntos(random.randint(0, ANCHO - 10), random.randint(-100, -40), random.randint(2, 6)) for _ in range(5)]
    #llamo la clase
    triangulo= Triangulo(200,100, 5)
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        # Limpiar pantalla
        pantalla.fill(NEGRO)
        # Mover y dibujar el triangulo
        triangulo.mover(pygame.key.get_pressed())
        triangulo.dibujar()

        
        # Mover y dibujar los puntos rojos
        for punto in puntos_rojos:
            punto.mover()
            punto.dibujar()
        

        # Actualizar pantalla
        pygame.display.flip()
        reloj.tick(FPS)

    pygame.quit()

# Iniciar el juego
if __name__ == "__main__":
    main()
