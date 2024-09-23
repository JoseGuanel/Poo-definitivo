class Persona():

    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        
    #atributos(variables)
    #nombre="josé"
    #apellido="guanel"
    #edad=21
    #metodos (comportamientos)
    def hablar(self):
        print(f"{self.nombre} esta hablando")

    def caminar(self):
        print(f"{self.nombre} esta caminando")

#instancioando la clase (creando objetos)
persona1=Persona("josé","guanel",21)
persona2=Persona("victor","saldivia",28)

#acceso a los atributos y metodos del objeto
print(f"nombre:{persona1.nombre}")
print(f"apellido:{persona1.apellido}")
print(f"edad:{persona1.edad}")

persona1.hablar()
persona2.caminar()