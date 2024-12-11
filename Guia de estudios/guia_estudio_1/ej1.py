#ejercicio de estudio n1
"""Implementar un programa que gestione la información de un grupo de estudiantes. Cada
estudiante tendrá un nombre y un promedio de notas. Además, el sistema debe determinar
si el estudiante ha aprobado o no, y permitir la actualización de sus notas de forma
controlada.

Instrucciones:
1. Implementar la clase Estudiante con los atributos privados (nombre y promedio) y
atributo público (estado) que debe indicar si el estudiante ha aprobado o no
(Booleano)

2. El programa debe permitir la creación de al menos tres estudiantes con su
respectivo nombre y promedio.

3. Imprimir el estado de cada estudiante utilizando un método mágico para mostrar su
nombre y promedio.

4. Simular una actualización de notas utilizando un método para ello.
5. Evaluar si los estudiantes han aprobado llamando a un método para evaluar el estado
del estudiante, y que muestre un mensaje con su estado de aprobación"""

class Estudiantes(): # iniciamos la classe estudiante 
    def __init__(self,__nombre,__promedio): # el contructor donde dice qye pongamios en privado 
        self.__nombre=__nombre   # nombre y promedio
        self.__promedio=__promedio
        self.aprobado= False

    def __str__(self): # metodo magico que use para printear la cadena de texto de el nombre y el promedio
        return (f"El nombre de la estudiante es {self.__nombre} y el promedio {self.__promedio}.")
    
    def actualizacion_de_notas(self,nuevo_promedio): # creamos metodo magico para poder actualizar las notas
        self.__promedio=nuevo_promedio # la variable privada de promedio se queda guarada en nuevo promedio 
        return print(f"El promedio se actualiza a {self.__promedio} de {self.__nombre}.") # retornamos el mensje de actualizacion
    
    def estado_de_aprobacion (self): # que hice aqui 
        
        if self.__promedio>= 40:  #lo que hice si el promedio del estudiante es mayor o = a 40 entonces aprueba y el aprobado es true
            self.aprobado=True
            print(f"El estudiante {self.__nombre} a aprobado con un promedio de {self.__promedio}") # printeamos mensaje
        else:
            self.aprobado=False   #si no aprubea se queda el false y printeamos el mensjes de reprobado
            print(f"El estudiante {self.__nombre} a sido reprobado con un promedio de {self.__promedio}.")


#creacion de los objetos ( estudiantes)
estudiante1=Estudiantes("percy",35,)
estudiante2=Estudiantes("atenea",67)
estudiante3=Estudiantes("afrodita",45)

#printeo el estado de losm estudiantes 
print(estudiante1)
print(estudiante2)
print(estudiante3)

#llamo a la funcion de eestado de aprobacion para que me de si aprobo o no
estudiante1.estado_de_aprobacion()
estudiante2.estado_de_aprobacion()
estudiante3.estado_de_aprobacion()

#llamo a la funcion de actualizacion de notas y en el parentesis pongo la nota actualizada 
estudiante1.actualizacion_de_notas(56)

# y para finalizar verificamo0s el estado del estudiante 
estudiante1.estado_de_aprobacion()


